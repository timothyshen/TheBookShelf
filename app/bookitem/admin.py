from django.contrib import admin

# Register your models here.
from .models import Book, BookCategory, Chapter, Comment

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Chapter)
admin.site.register(Comment)
