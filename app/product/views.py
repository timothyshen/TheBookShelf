import json
from rest_framework.serializers import Serializer
import stripe

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from stripe import webhook
from stripe.api_resources import line_item

from .models import Top_up_item, Subscription_Plan, User_profile
from .serializers import TopUpItemSerializer, SubscriptionSerializer, UserProfileSerializer


# Create your views here.

class TopUpView(generics.ListAPIView):
    serializer_class = TopUpItemSerializer
    queryset = Top_up_item.objects.all()
    permission_classes = [AllowAny]


class SubscriptionView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription_Plan.objects.filter(is_featured=True)
    permission_classes = [AllowAny]


class UserProfileView(APIView):

    def get_object(self, pk):
        return User_profile.objects.get_or_create(pk=pk, plan_id=3)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def upgrade_account(request):
#     user_profile = User_profile.objects.get(user_id=request.user.id)
#     print(request.data, user_profile)
#     # plan = request.data['plan']
#     # change_plan = ''
#     # print('Plan', plan)
#     plan = Subscription_Plan.objects.get(title='1 month VIP')
#     # if plan == '1 month VIP':
#     #     plan = Subscription_Plan.objects.get(title='1 month VIP')
#     # elif plan == '3 month VIP':
#     #     change_plan = Subscription_Plan.objects.get(title='3 month VIP')
#     # elif plan == '6 month VIP':
#     #     change_plan = Subscription_Plan.objects.get(title='6 month VIP')
#     # elif plan == '12 month VIP':
#     #     change_plan = Subscription_Plan.objects.get(title='12 month VIP')
#     print(type(plan))
#     user_profile.plan = plan
#     user_profile.save()
#
#     serializer = UserProfileSerializer(user_profile)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def cancel_plan(request):
#     user_profile = User_profile.objects.get(user_id=request.user.id)
#     plan_free = Subscription_Plan.objects.get(title='Free')
#
#     user_profile.plan = plan_free
#     user_profile.plan_status = user_profile.PLAN_INACTIVE
#     user_profile.save()
#
#     # try:
#     #     stripe.api_key = settings.STRIPE_SECRET_KEY
#     #     stripe.Subscription.delete(user_profile.stripe_subscription_id)
#     # except Exception:
#     #     return Response({'error': 'Something went wrong. Please try again'})
#
#     serializer = UserProfileSerializer(user_profile)
#     return Response(serializer.data)
