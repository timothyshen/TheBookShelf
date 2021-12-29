from django.db.models import Count
from django.db.models import F
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, BookCategory, Chapter
from .serializers import BookSerializer, CategorySerializer, ChapterSerializer, AuthorChapterDetailSerializer, \
    ChapterDetailSerializer


# Create your views here.


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class ChapterListView(ListAPIView):
    serializer_class = ChapterDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Chapter.objects.filter(book_id=self.kwargs.get('book_id', None))


class BookCategoryDetailView(ListAPIView):
    queryset = BookCategory.objects.annotate(total_number=Count('genre'))
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        queryset1 = Book.objects.annotate(chapter_count=Count('chapter'),
                                          total_words=Sum(Coalesce(F('chapter__word_count'), 0)))
        return queryset1

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.id).update(total_click=F('total_click') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ChapterDetailView(RetrieveAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny, ]

    def get_object(self):
        return Chapter.objects.get(book_id=self.kwargs.get('book_id', None), id=self.kwargs.get('chapter_id', None))


class AuthorBookViewSet(ListCreateAPIView):
    serializer_class = BookSerializer

    # permission_classes = (IsAuthorPermission,)
    def get_queryset(self):
        return Book.objects.filter(book_author=self.request.user)


class AuthorBookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # permission_classes = (IsAuthorPermission,)


class AuthorChapterView(ListCreateAPIView):
    serializer_class = AuthorChapterDetailSerializer

    # permission_classes = (IsAuthorPermission,)

    def get_queryset(self):
        return Chapter.objects.filter(book_id=self.kwargs.get('book_id', None))


class AuthorChapterDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorChapterDetailSerializer

    # permission_classes = (IsAuthorPermission,)

    def get_object(self):
        return Chapter.objects.get(book_id=self.kwargs.get('book_id', None), id=self.kwargs.get('chapter_id', None))


#


