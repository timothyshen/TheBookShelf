# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '03/06/2021 11:53'

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from user.models import AuthUser
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    用户注册信息序列化
    """

    class Meta:
        model = AuthUser
        fields = ('email', 'username', 'password', 'first_name')
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
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = AuthUser
        fields = (
            'email',
            'password',
            'refresh',
            'access',
            'role'
        )
        depth = 1

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user_email = authenticate(email=email, password=password)

        if user_email is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user_email)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user_email)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user_email.email,
                'full_name': user_email.get_full_name(),
                'role': user_email.role,
            }

            return validation
        except AuthUser.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


# class CustomJWTSerializer(TokenObtainPairSerializer):
#
#     def get_token(cls, user):
#         token = super(CustomJWTSerializer, cls).get_token(user)
#
#         token['username'] = user.username
#         return token
#
#     def validate(self, attrs):
#         credentials = {
#             'username': '',
#             'password': attrs.get("password")
#         }
#
#         user_obj = AuthUser.objects.filter(email=attrs.get("username")).first() or AuthUser.objects.filter(
#             username=attrs.get("username")).first()
#
#         if user_obj:
#             credentials['username'] = user_obj.username
#
#         return super().validate(credentials)
