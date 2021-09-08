from rest_framework import serializers
from .models import Transaction_History,Income_History,Author_Pool

#Transaction_History序列化
class Transaction_History_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction_History
        fields = "__all__"

#Income_History序列化
class Income_History_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Income_History
        fields = "__all__"

#Author_Pool序列化
class Author_Pool_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Author_Pool
        fields = "__all__"
