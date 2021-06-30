# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '30/06/2021 22:59'

from .views import TopUpView, SubscriptionView, UserProfileView
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("topup", TopUpView.as_view(), name='get_top_up'),
    path("subscription", SubscriptionView.as_view(), name='get_subscription'),
    path("user_profile", UserProfileView.as_view(), name='User_profile')
]
