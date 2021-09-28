from datetime import timezone

from django.db import models

# Create your models here.
from django.urls import reverse

from TheBookshelf import settings
from user.models import AuthUser
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BookCategory(models.Model):
    category_name = models.CharField(default="", max_length=30, verbose_name='Category name')
    category_code = models.CharField(default="", max_length=30, verbose_name='Category code')
    is_tab = models.BooleanField(default=False, verbose_name='is Navigate')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Added time')

    class Meta:
        verbose_name = 'Type Category'
        verbose_name_plural = 'Type categories'
        db_table = 'Book Genre'

    def __str__(self):
        return self.category_name


def image_upload_path(instance, fileanme):
    return settings.MEDIA_ROOT + '/book/%Y/%m/{0}/{1}'.format(instance.book_name, fileanme)


class Book(models.Model):
    BOOK_STATUS = (
        ('Ongoing', u'Ongoing'),
        ('Completed', u'Completed')
    )
    title = models.CharField(default="", max_length=30, verbose_name='Book title', unique=True)
    cover_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    status = models.CharField(choices=BOOK_STATUS, default='Ongoing', verbose_name='Status', max_length=150,
                              null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               verbose_name='author',
                               related_name='author',
                               null=True)
    genre = models.ForeignKey(BookCategory,
                              on_delete=models.CASCADE,
                              verbose_name='book type',
                              related_name='genre',
                              null=True)
    short_description = models.TextField(verbose_name='Short description', default='')
    description = models.TextField(verbose_name='Book Description', default='')

    # non-editable values
    total_vote = models.IntegerField(verbose_name='Total vote', default=0, editable=False)
    total_click = models.IntegerField(verbose_name='Total Click', default=0, editable=False)
    fav_num = models.IntegerField(verbose_name='Total favorite number', default=0, editable=False)
    added_time = models.DateTimeField(verbose_name='Added time', auto_now_add=True, editable=False)
    last_update = models.DateTimeField(verbose_name='last update', auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_book_name(self):
        return self.title

    class Meta:
        db_table = 'Book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Chapter(models.Model):
    PUBLISH_STATUS = (
        ('Published', u'Published'),
        ('Draft', u'Draft'),
        ('Trash', u'Trash'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='book', null=True, related_name='chapter')
    title = models.CharField(verbose_name='Chapter title', default='', max_length=150)
    body = models.TextField(verbose_name='Chapter text', default='')
    word_count = models.IntegerField(verbose_name='Word count', default=0)
    created_time = models.DateTimeField(verbose_name='Created time', auto_now_add=True, editable=False)
    last_update = models.DateTimeField(verbose_name='last update', auto_now=True, editable=False)
    publish_status = models.CharField(choices=PUBLISH_STATUS, default='Published', max_length=150)
    is_vip = models.BooleanField(verbose_name='VIP chapter', default=False)
    coin_price = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Chapter'
        verbose_name = 'chapter'
        verbose_name_plural = 'chapters'

#
