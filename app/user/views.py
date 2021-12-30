import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UsersSerializer
from rest_framework import permissions
from .models import AuthUser


class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # print(request.data)
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            # print(new_user.email)
            if new_user:
                # add these
                r = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                    'username': new_user.email,
                    'password': request.data['password'],
                    'client_id': 'IFEP4IQWLwwg1hhsE2hykjDMKbyibWJnvy7spiEw',
                    'client_secret': 'xsEJ3jLIlJhTs4ZMFzad2z2I8z3Pzcxq5h8zdHu09VLokFoj8a2dbD3zbsuYvCd6ooKId0vid8TAkPAUqIAxF1JsWNgoRyc7W3ZMVA6RgYaZ3VQ8u81tbar0BoXfVVMz',
                    'grant_type': 'password'
                })
                return Response(r.json(), status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AuthUser.objects.all()
    serializer_class = UsersSerializer


class ReaderLoginView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)


class AuthorLoginView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        if serializer.data['role'] == 2:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "You need to be an Author in order to log in"}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = AuthUser.objects.all()
    serializer_class = UsersSerializer
