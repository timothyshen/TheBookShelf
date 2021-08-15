from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentPublicView
)

urlpatterns = [
    url(r'^book/comment$', CommentPublicView.as_view(), name='list'),
]
