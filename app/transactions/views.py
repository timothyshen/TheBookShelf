# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import User_profile
from user.models import AuthUser
from transactions.models import Transaction_History,Income_History,Author_Pool
from transactions.serializers import Transaction_History_Serializers,Income_History_Serializers,Author_Pool_Serializers

#获得当前余额
def get_balance(self):
    data = self.request.data
    balance = User_profile.objects.get(id=data['user'])
    return balance

