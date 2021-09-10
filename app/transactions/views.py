# Create your views here.

from django.http import Http404, QueryDict
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Top_up_item, User_profile
from transactions.models import Transaction_History, Income_History, Author_Pool
from transactions.serializers import Transaction_History_Serializers, Income_History_Serializers, \
    Author_Pool_Serializers
from rest_framework.permissions import IsAuthenticated
from bookitem.models import Chapter


# 根据用户ID获得用户的Transactions记录[GET]/[POST]
class Transaction_HistoryView(ListCreateAPIView):
    # 登录验证
    permission_classes = [IsAuthenticated]
    # 序列化
    serializer_class = Transaction_History_Serializers

    # 检测当前登录用户
    def get_queryset(self):
        return Transaction_History.objects.filter(user=self.request.user.id)

    def post(self, request, *args, **kwargs):
        data = QueryDict(request.data.urlencode(), mutable=True)
        # 自动根据item赋值price
        if len(data.get('item')) > 0:
            item = Top_up_item.objects.get(id=data['item'])
            price = item.book_coin
            data.update({'price': price})

        # 自动根据chapter赋值price
        elif len(data.get('chapter')) > 0:
            chapter = Chapter.objects.get(id=data['chapter'])
            coins = chapter.coin_price
            data.update({'price': coins})

        # ---------获取NEW_BALANCE-----------
        user = User_profile.objects.get(user=data.get('user', None))
        user_balance = int(user.balance)
        data.update({'New_balance': user_balance - int(data.get('price', None))})
        # ----------------------------------

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


# 根据Transactions_ID 进行单次查询 (所有人可查.透明化) [GET][无法修改故不做/Update or Delete]
class Transaction_History_DetailsView(ListAPIView):
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
class Author_PoolView(ListCreateAPIView):
    # 登录验证
    permission_classes = [IsAuthenticated]
    # 序列化
    serializer_class = Author_Pool_Serializers

    # 检测当前登录用户
    def get_queryset(self):
        return Author_Pool.objects.filter(Author_id=self.request.user.id)
