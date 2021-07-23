# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '03/06/2021 11:53'

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from oauth2_provider.models import RefreshToken
# from oauth2_provider.oauth2_validators import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken

from user.models import AuthUser
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    用户注册信息序列化
    """

    class Meta:
        model = AuthUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    """
    所有用户名单的序列化
    """

    class Meta:
        model = AuthUser
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    """
    用户登入序列化
    """
    class Meta:
        model = AuthUser
        fields = '__all__'
