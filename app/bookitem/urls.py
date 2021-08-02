# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/07/2021 23:03'

from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter

from bookitem.views import BookCategoryDetailView, BookListView, BookDetailView, AuthorBookViewSet, \
    AuthorBookDetailView, TopBookByAttribute, TopBookByCategory

router = DefaultRouter()

urlpatterns = [
    path('all-category', BookCategoryDetailView.as_view(), name='all-category'),
    path('detail', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author/book/', AuthorBookViewSet.as_view(), name="author-book"),
    path('author/book/<int:pk>/', AuthorBookDetailView.as_view(), name='author-detail'),
    path('ranking/attribute/', TopBookByAttribute, name='ranking-attribute'),
    path('ranking/category/', TopBookByCategory, name='ranking-category'),
]
