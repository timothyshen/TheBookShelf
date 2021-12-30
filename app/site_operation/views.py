from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from bookitem.models import Book
from bookitem.serializers import BookSerializer
from .models import IndexImage, IndexPage
from .serializers import IndexImageSerializer, IndexPageSerializer


# Create your views here.

class IndexPageView(ModelViewSet):
    serializer_class = IndexPageSerializer

    def get_queryset(self):
        return IndexPage.objects.filter(activation='Active')


class IndexImageView(ModelViewSet):
    serializer_class = IndexImageSerializer
    queryset = IndexImage.objects.all()

class TopBookValueViewSet(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        request_item = self.kwargs.get('request_item', None)
        return Book.objects.annotate(Count(request_item)).order_by('-' + request_item)[:10]


class TopBookByCategory(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        request_item = self.kwargs.get('request_item', None)
        request_category = self.kwargs.get('request_category', None)
        return Book.objects.filter(book_type__category_name=request_category).annotate(Count(request_item)).order_by('-' + request_item)[:10]
