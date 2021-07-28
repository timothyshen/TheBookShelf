from rest_framework import serializers
from .models import Book, BookCategory, Chapter, Comment
from .filters import CustomerHyperlink


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
        fields = ('url', 'id', 'chapter_title', 'book')


class BookSerializer(serializers.ModelSerializer):
    chapter = ChapterDetailSerializer(many=True, read_only=True)
    book_author = serializers.PrimaryKeyRelatedField(read_only=True, source='book_author.username')
    chapter_count = serializers.IntegerField(read_only=True)
    total_words = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        rep['book_type'] = instance.book_type.category_name
        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
