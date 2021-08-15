from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializer import *


# Create your views here.
class BookcaseView(ListCreateAPIView):
    # permission_classes = IsAuthenticated
    serializer_class = BookCaseSerializer

    def get_queryset(self):
        return Bookcase.objects.filter(user_id=self.request.user)


class BookMarkView(CreateAPIView):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()
    # permission_classes = IsAuthenticated
