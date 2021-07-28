# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '27/07/2021 18:32'

from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Chapter


class CustomerHyperlink(serializers.HyperlinkedIdentityField):
    view_name = 'chapter-detail'

    # queryset = Chapter.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'book_id': obj.book_id,
            'chapter_id': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'book_id': view_kwargs['book_id'],
            'pk': view_kwargs['chapter_id']
        }
        return self.get_queryset().get(**lookup_kwargs)
