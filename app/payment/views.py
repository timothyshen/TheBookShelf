import json

from django.views.decorators.http import require_POST
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


class BillingAddressListView(generics.ListAPIView):
    serializer_class = BillingAddressSerializer
    queryset = Billing_address.objects.all()


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

    # billing_address = BillingAddressSerializer(data['billing'])
    gateway = data['gateway']
    product_type = data['product_type']
    user_profile = User_profile.objects.get(user__in=[data['user']])
    if gateway == 'stripe':
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=user_profile.user.uid,
                success_url='http://127.0.0.1:8000/payment/success/?session_id={CHECKOUT_SESSION_ID}&success=true',
                cancel_url='http://127.0.0.1:8000/?canceled=true',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1
                    }
                ]
            )
            return Response({'sessionId': checkout_session['id']})
        except Exception as e:
            return Response({'error': str(e)})


@api_view(['POST'])
def create_topup_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    print(request.user)
    if data['product']:
        price_id = 'price_1JF4FxBaL13HgkoymjNPtsCs'
    gateway = data['gateway']
    product_type = data['product_type']
    billing_id = create_billing(data['billing_address'])
    order = {
        'user_id': request.user.id,
        'billing_address_id': billing_id

    }
    print(billing_id)
    print(order)
    order_info = OrderSerailzier(data=order)
    if order_info.is_valid():
        order_info.save()

    return HttpResponse(status=200)
    # if gateway == 'stripe' and product_type == 'topup':
    #     try:
    #         checkout_session = stripe.checkout.Session.create(
    #             client_reference_id=user_profile.user.uid,
    #             success_url='http://127.0.0.1:8000/payment/success/?session_id={CHECKOUT_SESSION_ID}&success=true',
    #             cancel_url='http://127.0.0.1:8000/?canceled=true',
    #             payment_method_types=['card'],
    #             mode='payment',
    #             line_items=[
    #                 {
    #                     'price': price_id,
    #                     'quantity': 1
    #                 }
    #             ]
    #         )
    #         return Response({'sessionId': checkout_session['id']})
    #     except Exception as e:
    #         return Response({'error': str(e)})


def create_billing(billing):
    serializer = BillingAddressSerializer(data=billing)

    if serializer.is_valid():
        billing = serializer.save()
        # print(serializer.data)
        # print(serializer.data['id'])
        # billing_address.save()
        return serializer.data['id']


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''
    print(request.data)
    print(request.user)
    print()

    try:
        user_profile = User_profile.objects.get(user__in=[request.user])
        subscription = stripe.Subscription.retrieve(user_profile.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)
        user_profile.plan_status = user_profile.PLAN_ACTIVE
        user_profile.plan_end_date = datetime.fromtimestamp(subscription.current_period_end)
        user_profile.plan = Subscription_Plan.objects.get(title=product.name)
        user_profile.save()
        serializer = UserSerializer(user_profile)
        print('serializer', serializer)
        return Response(serializer.data)
    except Exception as e:
        error = 'There something wrong. Please try again!'

        return Response({'error': error, 'description': e})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    # print('payload', payload)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
        # ... handle other event types
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        user = User_profile.objects.get(user__uid=session.get('client_reference_id'))
        user.stripe_customer_id = session.get('customer')
        user.stripe_subscription_id = session.get('subscription')
        user.save()

    return HttpResponse(status=200)
