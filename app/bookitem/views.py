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
from .serializers import BookSerializer, CategorySerializer, ChapterSerializer


# Create your views here.


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class ChapterListView(ListAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Chapter.objects.filter(book_id=self.kwargs.get('book_id', None))


class BookCategoryDetailView(ListAPIView):
    queryset = BookCategory.objects.annotate(total_number=Count('books'))
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


class AuthorBookViewSet(APIView):
    serializer_class = BookSerializer

    # permission_classes = (IsAuthorPermission,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        print(request.user)
        try:
            book = Book.objects.filter(book_author=self.request.user.id)
            serializers_book = BookSerializer(Book)
            return Response(serializers_book.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'you are not an author'})


class AuthorBookDetailView(APIView):
    serializer_class = BookSerializer

    # permission_classes = (IsAuthorPermission,)

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorChapterView(APIView):
    serializer_class = ChapterSerializer

    # permission_classes = (IsAuthorPermission,)

    def get(self, request, format=None):
        chapter = Chapter.objects.filter(book_id=self.request.query_params.get('book_id', None))
        serializer = self.serializer_class(data=chapter)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorChapterDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChapterSerializer

    # permission_classes = (IsAuthorPermission,)

    def get_queryset(self):
        return Chapter.objects.get(book_id=self.kwargs.get('book_id', None), id=self.kwargs.get('chapter_id', None))


#


@api_view(['POST'])
def TopBookByCategory(request):
    data = request.data
    request_item = data['request_item']
    request_category = data['requestCategory']
    return Book.objects.filter(book_type__category_name=request_category).annotate(Count(request_item)).order_by(
        '-' + request_item)[:10]


@api_view(['POST'])
def TopBookByAttribute(request):
    data = request.data
    request_item = data['request_item']
    return Book.objects.annotate(Count(request_item)).order_by('-' + request_item)[:10]
