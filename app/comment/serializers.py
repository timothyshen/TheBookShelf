# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '12/08/2021 22:17'

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField

from .models import Comment


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = [
            'parent'
        ]


class CommentSerializer(serializers.ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='comment:list')
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()
    created_on = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=['%d-%m-%Y %H-%M-%S', 'iso-8601'])

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
