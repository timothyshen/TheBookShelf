from django.db.models import Count
from django.db.models import F
from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorPermission
from .serializers import *


# Create your views here.


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterListView(ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.filter(book_id=self.kwargs.get('book_id', None))


class BookCategoryDetailView(ListAPIView):
    queryset = BookCategory.objects.annotate(total_number=Count('books'))
    serializer_class = CategorySerializer


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer

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

    def get_object(self):
        return Chapter.objects.get(book_id=self.kwargs.get('book_id', None), id=self.kwargs.get('chapter_id', None))


class AuthorBookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    # permission_classes = (IsAuthorPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"status": True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.id = kwargs.get('pk')
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({"status": True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return serializer.save(book_author=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(book_author=self.request.user)


class AuthorChapterViewSet(ModelViewSet):
    serializer_class = ChapterSerializer

    # permission_classes = (IsAuthorPermission,)

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        print(book_id)
        return Chapter.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        return serializer.save(book_id=self.kwargs['book_id'])


class TopBookValueViewSet(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        request_item = self.kwargs.get('request_item', None)
        return Book.objects.annotate(Count(request_item)).order_by('-' + request_item)[:10]


@api_view(['POST'])
def TopBookByCategory(request):
    data = request.data
    request_item = data['request_item']
    request_category = data['requestCategory']
    return Book.objects.filter(book_type__category_name=request_category).annotate(Count(request_item)).order_by(
        '-' + request_item)[:10]
