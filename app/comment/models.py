from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.urls import reverse

from bookitem.models import Book
from user.models import AuthUser


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(verbose_name='Created time', auto_now_add=True, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_commnet')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    likes = models.ManyToManyField(AuthUser, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(AuthUser, blank=True, related_name='comment_dislikes')

    objects = CommentManager()

    class Meta:
        db_table = 'Comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-created_on']

    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
