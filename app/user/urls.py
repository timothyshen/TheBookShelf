#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '03/06/2021 20:22'

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from .serializers import CustomJWTSerializer
from .views import (
    AuthUserRegisterView,
    AuthUserLoginView,
    UserListView,
    # MyObtainTokenPairView
)

urlpatterns = [
    path('register', AuthUserRegisterView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    path('users', UserListView.as_view(), name='users')
]
