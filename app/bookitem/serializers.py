from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from wagtail.images.api.fields import ImageRenditionField
from user.models import AuthUser
from .models import Book, BookCategory, Chapter
from .filters import CustomerHyperlink
from wagtail.images import get_image_model

class wagtailImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = get_image_model()
        fields = ('file','url')

    def get_url(self, obj):
        return obj.file.url

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ('id', 'username')

class CategorySerializer(serializers.ModelSerializer):
    total_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookCategory
        fields = ('id', 'category_name', 'category_code', "is_tab", 'add_time', 'total_number')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class ChapterDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = CustomerHyperlink(
        view_name='chapter-detail'
    )

    class Meta:
        model = Chapter
        fields = ('url', 'id', 'title', 'book')


class BookSerializer(serializers.ModelSerializer):
    chapter = ChapterDetailSerializer(many=True, read_only=True)
    chapter_count = serializers.IntegerField(read_only=True)
    total_words = serializers.IntegerField(read_only=True)
    author = AuthorSerializer(read_only=True)
    cover_photo = wagtailImageSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super(BookSerializer, self).to_representation(instance)
    #     rep['book_type'] = instance.book_type.category_name
    #     return rep


class AuthorChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
