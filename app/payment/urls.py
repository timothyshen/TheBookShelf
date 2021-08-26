# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/07/2021 23:03'

from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter

from .views import get_stripe_pub_key, check_session, create_checkout_session, \
    OrderView, BillingAddressListView, BillingAddressDetailView, OrderDetailView
from .webhook import stripe_webhook

router = DefaultRouter()

urlpatterns = [
    path('stripe/get_stripe_pub_key/', get_stripe_pub_key, name='get_stripe_pub_key'),

    path('stripe/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    path('stripe/check_session/', check_session, name='check_session'),
    path('order/', OrderView.as_view(), name='order_create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_create'),
    path('billing', BillingAddressListView.as_view(), name='billing_create'),
    path('billing/<int:pk>/', BillingAddressDetailView.as_view(), name='billing_detail'),
    path('', include(router.urls)),
]
