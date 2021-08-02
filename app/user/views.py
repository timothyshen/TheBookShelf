import generic as generic
from django.shortcuts import render
from rest_framework import status, generics
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
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED

            r = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                'username': serializer.data['email'],
                'password': request.data['password'],
                'client_id': 'CuHSbKKrPUwL0IzeRZ5M8CnTVrGav58BW9m75M9v',
                'client_secret': 'kMX4H5mGCSGBgmhDTfi8vYLfU8SRfqBWx5F4IpFgtEKIjBcvLdc6oUImZ2rLVKPAgznY4mjMf9s8k67QYK1E9fzDrsdjw2dzYVXcLPzecSW4OWOV3DCfuTWD8lWQKRPo',
                'grant_type': 'password',
            })
            return Response(r.json(), status=status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserLoginView(APIView):
    """
    用户登入api接口
    """
    serializer_class = UserLoginSerializer

    def get(self, request):
        serializer = self.serializer_class(self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = True
        data = request.data
        user = AuthUser.objects.filter(id=request.user.id)
        serializer = self.serializer_class(user, data=data, many=True, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)


class UserListView(generics.ListAPIView):
    """
    用户名单提取api接口
    """
    serializer_class = UserListSerializer
    permission_classes = (AllowAny,)
    queryset = AuthUser.objects.all()


class AuthorLoginSerializer(APIView):
    serializer_class = UserLoginSerializer

    def get(self, request):
        serializer = self.serializer_class(self.request.user)
        if serializer.data['role'] == 2:
            return Response({'status': True, 'user': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'user': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
