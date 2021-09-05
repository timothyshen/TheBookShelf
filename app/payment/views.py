from datetime import datetime

import stripe
from django.conf import settings
from django.contrib import messages
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from bookitem.models import Chapter
from product.models import Subscription_Plan, Top_up_item
from product.models import User_profile
from .models import Order, Billing_address
from .serializers import BillingAddressSerializer, OrderSerailzier, PaymentUserSerializer, OrderDetailSerailzier
from .Price_id import filter_product


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerailzier
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerailzier
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class BillingAddressListView(generics.ListAPIView):
    serializer_class = BillingAddressSerializer
    queryset = Billing_address.objects.all()


class BillingAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BillingAddressSerializer
    permission_classes = [IsAuthenticated]
    queryset = Billing_address.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Billing_address.objects.get(pk=instance.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})


@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    print(request.user.id)
    userprofile = User_profile.objects.get(user__in=[request.user])
    gateway = data['gateway']
    billing_id = create_billing(data['billing_address'])
    order = {
        'user': request.user.id,
        'billing_address': billing_id,
        'product_name': data['product']

    }
    price_id = filter_product(data['product'])
    order_info = OrderSerailzier(data=order)
    if order_info.is_valid():
        order_info.save()
        print(order_info.data)
    if gateway == 'stripe':
        if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
            customer = stripe.Customer.retrieve(
                userprofile.stripe_customer_id)
            customer.sources.create(source=stripe.api_key)

        else:
            customer = stripe.Customer.create(
                email=request.user.email,
            )
            customer.sources.create(source=stripe.api_key)
            userprofile.stripe_customer_id = customer['id']
            userprofile.save()

        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=order_info.data['uuid'],
                success_url="http://localhost:8081/payment/success?session_id={"
                            "CHECKOUT_SESSION_ID}&success=true&order_id=%s&type=%s" % (
                            order_info.data['uuid'], data['type']),
                cancel_url='http://localhost:8081/?canceled=true',
                payment_method_types=['card'],
                mode=data['type'],
                customer=userprofile.stripe_customer_id,
                line_items=[
                    {
                        'price': data['price_id'],
                        'quantity': 1
                    }
                ]
            )
            current_order = Order.objects.get(uuid=checkout_session['client_reference_id'])
            current_order.payment_intent = checkout_session['payment_intent']
            current_order.paid_amount = checkout_session['amount_total']
            current_order.save()
            print(current_order)
            return Response({'sessionId': checkout_session['id']})

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            return Response({"message": f"{err.get('message')}"}, status=HTTP_400_BAD_REQUEST)

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(request, "Rate limit error")
            return Response({"message": "Rate limit error"}, status=HTTP_400_BAD_REQUEST)

        except stripe.error.InvalidRequestError as e:
            print(e)
            # Invalid parameters were supplied to Stripe's API
            return Response({"message": "Invalid parameters"}, status=HTTP_400_BAD_REQUEST)

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            return Response({"message": "Not authenticated"}, status=HTTP_400_BAD_REQUEST)

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            return Response({"message": "Network error"}, status=HTTP_400_BAD_REQUEST)

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            return Response({"message": "Something went wrong. You were not charged. Please try again."},
                            status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)})


def create_billing(billing):
    serializer = BillingAddressSerializer(data=billing)

    if serializer.is_valid():
        serializer.save()
        return serializer.data['id']


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''
    try:
        user_profile = User_profile.objects.get(user__in=[request.user])
        if request.data['type'] == 'subscription':
            subscription = stripe.Subscription.retrieve(user_profile.stripe_subscription_id)
            product = stripe.Product.retrieve(subscription.plan.product)
            user_profile.plan_status = user_profile.PLAN_ACTIVE
            user_profile.plan_end_date = datetime.fromtimestamp(subscription.current_period_end)
            user_profile.plan = Subscription_Plan.objects.get(title=product.name)
        elif request.data['type'] == 'payment':
            order = Order.objects.get(id=request.data['order_id'])
            coin_value = Top_up_item.objects.get(order.product_name)
            user_profile.balance += coin_value.book_coin
        user_profile.save()

        serializer = PaymentUserSerializer(user_profile)
        print('serializer', serializer)
        return Response(serializer.data)
    except Exception as e:
        error = 'There something wrong. Please try again!'

        return Response({'error': error, 'description': e})

