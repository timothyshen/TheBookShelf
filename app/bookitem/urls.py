# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/07/2021 23:03'

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookCategoryDetailView, BookListView, BookDetailView, AuthorBookViewSet, AuthorBookDetailView, \
    AuthorChapterView, ChapterDetailView, ChapterListView, \
    AuthorChapterDetailView

router = DefaultRouter()

urlpatterns = [
    path('all-category', BookCategoryDetailView.as_view(), name='all-category'),
    path('book', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:book_id>/chapter', ChapterListView.as_view(), name='book-chapter'),
    path('book/<int:book_id>/chapter/<int:chapter_id>', ChapterDetailView.as_view(), name='chapter-detail'),
    path('author/book/', AuthorBookViewSet.as_view(), name="author-book"),
    path('author/book/<int:pk>/', AuthorBookDetailView.as_view(), name='author-book-detail'),
    path('author/book/<int:book_id>/chapter', AuthorChapterView.as_view(), name='author-chapter-list'),
    path('author/book/<int:book_id>/chapter/<int:chapter_id>', AuthorChapterDetailView.as_view(),
         name='author-chapter-detail'),
    # path('book/comment', CommentPublicView.as_view(), name="book-comment-list"),
]
