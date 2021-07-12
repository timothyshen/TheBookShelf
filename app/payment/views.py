import json
from rest_framework.serializers import Serializer
import stripe
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from stripe import webhook
from stripe.api_resources import line_item

from .models import Order, Billing_address
from .serializers import BillingAddressSerializer, OrderSerailzier, UserSerializer
from product.models import User_profile
from rest_framework.permissions import IsAuthenticated

from product.models import Subscription_Plan


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerailzier
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class BillingAddressListView(generics.ListCreateAPIView):
    serializer_class = BillingAddressSerializer
    queryset = Billing_address.objects.all()
    permission_classes = [IsAuthenticated]


class BillingAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BillingAddressSerializer
    queryset = Billing_address.objects.all()
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})


@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    print(data)
    if data['plan']:
        price_id = 'price_1J8WjoBaL13HgkoyyGzH3ZBo'

    # # billing_address = BillingAddressSerializer(data['billing'])
    gateway = data['gateway']
    user_profile = User_profile.objects.get(user__in=[data['user']])
    if gateway == 'stripe':
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=user_profile.user.uid,
                success_url='payment/success/',
                cancel_url='http://127.0.0.1:8000/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1
                    }
                ]
            )
            order = OrderSerailzier(data)
            return Response({'sessionId': checkout_session['id']})
        except Exception as e:
            return Response({'error': str(e)})


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''

    try:
        user_profile = User_profile.objects.filter(user__in=[request.user])
        subscription = stripe.Subscription.retrieve(user_profile.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)

        user_profile.plan_status = user_profile.PLAN_ACTIVE
        user_profile.plan_end_date = datetime.fromtimestamp(subscription.current_period_end)
        user_profile.plan = Subscription_Plan.objects.get(name=product.name)
        user_profile.save()

        serializer = UserSerializer(user_profile)

        return Response(serializer.data)
    except Exception:
        error = 'There something wrong. Please try again!'

        return Response({'error': error})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    print('payload', payload)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        team = User_profile.objects.get(user__uid=session.get('client_reference_id'))
        team.stripe_customer_id = session.get('customer')
        team.stripe_subscription_id = session.get('subscription')
        team.save()

    return HttpResponse(status=200)
