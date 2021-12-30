from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError

from TheBookshelf import settings
from bookitem.models import Book


def image_upload_path(instance, fileanme):
    return settings.MEDIA_ROOT + '/index/%Y/%m/{0}/{1}'.format(instance.book.id, fileanme)


class IndexImage(models.Model):
    LINK_STATUS = (
        ('Inactive', u'Inactive'),
        ('Active', u'Active')
    )
    text = models.CharField(default='', max_length=1000, verbose_name='alt text')
    book_image = models.ImageField(default=u"media/image/default.png", max_length=1000, verbose_name='Book image', upload_to=image_upload_path,)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='index_book_image', verbose_name='book')
    activation = models.CharField(choices=LINK_STATUS, default='Inactive', verbose_name='Publish status',
                                  max_length=1000)

    def __str__(self):
        return "{0}/{1}".format(self.text, self.book.title)

    def save(self, *args, **kwargs):
        if not self.pk and IndexImage.objects.filter(activation='Active').count() >= 4:
            raise ValidationError('There are more than four actives')
        return super(IndexImage, self).save(*args, **kwargs)


class IndexPage(models.Model):
    LINK_STATUS=(
        ('Inactive', u'Inactive'),
        ('Active', u'Active')
    )
    promotion = models.CharField(default='', max_length=1000, verbose_name='promotion')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='home_page', verbose_name='book')
    activation = models.CharField(choices=LINK_STATUS, default='Inactive', verbose_name='Publish status', max_length=1000)

    def __str__(self):
        return "{0}/{1}".format(self.promotion, self.book.title)
