# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '13/08/2021 00:22'

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
    page_size = 10
