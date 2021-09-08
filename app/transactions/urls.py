# _*_ coding: utf-8 _*_

__author__ = 'Rick'
__date__ = '08/09/2021 17:03'

from .views import (
    TopUpView,
    SubscriptionView,
    UserProfileView,
    # cancel_plan,
    # upgrade_account,
)
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("topup/", TopUpView.as_view(), name='get_top_up'),
    path("subscription/", SubscriptionView.as_view(), name='get_subscription'),
    path("user_profile/", UserProfileView.as_view({'get': 'list'}), name='User_profile'),
    # path('account/upgrade_plan/', upgrade_account, name='upgrade_plan'),
    # path('account/cancel_plan/', cancel_plan, name='cancel_plan'),
]
