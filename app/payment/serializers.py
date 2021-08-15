# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '02/07/2021 21:29'

from .models import Order, Billing_address
from user.models import AuthUser
from product.models import Subscription_Plan, Top_up_item
from rest_framework import serializers


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription_Plan
        fields = (
            'title',
            'slug',
            'price'
        )


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_up_item
        fields = (
            'title',
            'slug',
            'price'
        )


class BillingAddressSerializer(serializers.ModelSerializer):
    user = PaymentUserSerializer(read_only=True)

    class Meta:
        model = Billing_address
        fields = "__all__"


class OrderDetailSerailzier(serializers.ModelSerializer):
    user = PaymentUserSerializer()
    billing_address = BillingAddressSerializer()

    class Meta:
        model = Order
        fields = "__all__"

class OrderSerailzier(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
