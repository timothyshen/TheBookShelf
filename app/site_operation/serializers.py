from rest_framework import serializers
from .models import *
from bookitem.serializers import BookSerializer, Book
from user.models import AuthUser

class BookForIndexSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, source='author.username')
    class Meta:
        model = Book
        fields=('id', 'title','cover_photo', 'author', 'short_description')



class IndexPageSerializer(serializers.ModelSerializer):
    book = BookForIndexSerializer()


    class Meta:
        model = IndexPage
        fields = '__all__'



class IndexImageSerializer(serializers.ModelSerializer):
    book = serializers.HyperlinkedIdentityField(view_name='book-detail')
    class Meta:
        model = IndexImage
        fields = '__all__'
