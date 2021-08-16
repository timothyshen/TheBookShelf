# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '25/07/2021 02:47'

import json

import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from TheBookshelf import settings
from payment.models import Order
from product.models import User_profile


@require_POST
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)
    print(event.data.object)
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print(payment_intent)
        current_order = Order.objects.get(payment_intent=payment_intent['id'])
        current_order.status = current_order.COMPLETED
        current_order.save()
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
        # ... handle other event types
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order = Order.objects.get(uuid=session.get('client_reference_id'))
        user = User_profile.objects.get(user_id=order.user_id)
        user.stripe_customer_id = session.get('customer')
        if session.get('subscription'):
            user.stripe_subscription_id = session.get('subscription')
        user.save()

    return HttpResponse(status=200)
