from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
import requests
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserListSerializer,
    # CustomJWTSerializer
)

from .models import AuthUser


class AuthUserRegisterView(APIView):
    """
    用户注册api接口
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            new_user = serializer.save()
            status_code = status.HTTP_201_CREATED

            r = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                'username': new_user.email,
                'password': request.data['password'],
                'client_id': 'CuHSbKKrPUwL0IzeRZ5M8CnTVrGav58BW9m75M9v',
                'client_secret': 'kMX4H5mGCSGBgmhDTfi8vYLfU8SRfqBWx5F4IpFgtEKIjBcvLdc6oUImZ2rLVKPAgznY4mjMf9s8k67QYK1E9fzDrsdjw2dzYVXcLPzecSW4OWOV3DCfuTWD8lWQKRPo',
                'grant_type': 'password',
            })
            return Response(r.json(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserLoginView(APIView):
    """
    用户登入api接口
    """
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'AuthUser logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)


class UserListView(APIView):
    """
    用户名单提取api接口
    """
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # user = request.user
        # if user.role != 1:
        #     response = {
        #         'success': False,
        #         'status_code': status.HTTP_403_FORBIDDEN,
        #         'message': 'You are not authorized to perform this action'
        #     }
        #     return Response(response, status.HTTP_403_FORBIDDEN)
        # else:
        users = AuthUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched users',
            'users': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)
