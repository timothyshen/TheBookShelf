from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializer import *


# Create your views here.
class BookcaseView(APIView):
    # permission_classes = IsAuthenticated

    def get_object(self, pk):
        try:
            return Bookcase.objects.get(pk=pk)
        except Bookcase.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bookcase = Bookcase.objects.filter(user_id=pk)
        return Response(bookcase)

    def post(self, request, pk, format=None):
        serializer = BookCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookMarkView(CreateAPIView):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()
    # permission_classes = IsAuthenticated
