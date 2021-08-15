import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UsersSerializer
from rest_framework import permissions
from .models import AuthUser


class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                # add these
                r = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                    'username': new_user.email,
                    'password': request.data['password'],
                    'client_id': 'BlVMKZ9ZDGg3t6kiHw88YoyOsYFro31RtIM3Wmqe',
                    'client_secret': 'LhRlZjzFJje9g8UahoRFfjg9AFqIbycxuOpS3xLyJ8ZBMF6z8Fcy9Md9C8yoQsb15EV3X4cQU0MeKHANxLZKyDyRkGoAya7TkCc1FEzBo47UIIwRdwMVP16R2leeOHRf',
                    'grant_type': 'password'
                })
                return Response(r.json(), status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AuthUser.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)
