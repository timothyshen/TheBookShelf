from django.contrib import admin

# Register your models here.
from .models import Book, BookCategory, Chapter
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author')


class ChapterAdmin(ModelAdmin):
    model = Chapter
    add_to_settings_menu = False
    exclude_from_explorer = False
    menu_label = 'Chapter'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    list_display = ('title', 'book')
    list_filter = ('title',)
    search_fields = ('title', 'book')


class GenreAdmin(ModelAdmin):
    model = BookCategory
    menu_label = 'Genre'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    list_display = ('category_name',)
    list_filter = ('is_tab',)
    search_fields = ('category_name',)


class NovelGroup(ModelAdminGroup):
    menu_label = 'Novels'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BookAdmin, ChapterAdmin, GenreAdmin)


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(NovelGroup)
