# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import User_profile
from transactions.models import Transaction_History, Income_History, Author_Pool
from transactions.serializers import Transaction_History_Serializers, Income_History_Serializers, \
    Author_Pool_Serializers
from rest_framework.permissions import IsAuthenticated


# 获得当前余额
def get_balance(self):
    data = self.request.data
    balance = User_profile.objects.get(id=data['user'])
    return balance


# 根据用户ID获得用户的Transactions记录[GET]
class Transaction_HistoryView(ListAPIView):
    # 登录验证
    permission_classes = [IsAuthenticated]
    # 序列化
    serializer_class = Transaction_History_Serializers

    # 检测当前登录用户
    def get_queryset(self):
        return Transaction_History.objects.filter(user=self.request.user.id)


# 根据Transactions_ID 进行单次查询 (所有人可查.透明化) [GET]
class Transaction_History_DetailsView(APIView):
    def get_object(self, transaction_id):
        try:
            return Transaction_History.objects.get(pk=transaction_id)
        except Transaction_History.DoesNotExist:
            raise Http404

    def get(self, request, transaction_id, format=None):
        Transaction = self.get_object(transaction_id)
        serializer = Transaction_History_Serializers(Transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 根据用户ID获得用户的Income记录 [GET]
class Income_HistoryView(ListAPIView):
    # 登录验证
    permission_classes = [IsAuthenticated]
    # 序列化
    serializer_class = Income_History_Serializers

    # 检测当前登录用户
    def get_queryset(self):
        return Income_History.objects.filter(Author_id=self.request.user.id)


# 根据用户ID获得用户的收益池 [GET]
class Author_PoolView(ListAPIView):
    # 登录验证
    permission_classes = [IsAuthenticated]
    # 序列化
    serializer_class = Author_Pool_Serializers

    # 检测当前登录用户
    def get_queryset(self):
        return Author_Pool.objects.filter(Author_id=self.request.user.id)
