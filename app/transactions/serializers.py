from rest_framework import serializers

from product.models import User_profile
from .models import Transaction_History, Income_History, Author_Pool


# Transaction_History序列化
class Transaction_History_Serializers(serializers.ModelSerializer):
    # 给status赋值
    status = serializers.CharField(read_only=True)
    # 给user赋值
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    # 检测余额是否不足 & 不能为负数或0的转账/交易
    def validate(self, data):
        # 获取当前提交的价格
        if data.get('price') is None:
            price = 0
        else:
            price = float(data.get('price', None))
        # 获取用户的余额
        user = User_profile.objects.get(user=data.get('user'))
        user_balance = float(user.balance)
        # 余额不足错误
        if price > user_balance:
            raise serializers.ValidationError("No Enough Creader Coins!")
        # 金额为0以下错误
        elif price <= 0:
            raise serializers.ValidationError("Invalid Amount or Price")
        # 同时有item和chapter
        elif data.get('chapter', None) and data.get('item', None) is not None:
            raise serializers.ValidationError("Unexpected Error,Please check your purchase")
        # 转账给自己错误
        elif data.get('user') == data.get('to_user') and data.get('Transaction_type') == 'Transfer':
            raise serializers.ValidationError("You cannot transfer to yourself")
        return data


    class Meta:
        model = Transaction_History
        fields = "__all__"


# Income_History序列化
class Income_History_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Income_History
        fields = "__all__"


# Author_Pool序列化
class Author_Pool_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Author_Pool
        fields = "__all__"
