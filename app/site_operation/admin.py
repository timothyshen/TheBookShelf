from django.contrib import admin

# Register your models here.
from .models import IndexImage, IndexPage
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

class IndexImageAdmin(ModelAdmin):
    model = IndexImage
    menu_label = 'Index Image'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('text', 'book_image', 'book')
    list_filter = ('activation',)
    search_fields = ('text',)

class IndexPageAdmin(ModelAdmin):
    model = IndexPage
    menu_label = 'Index Page'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('promotion', 'book', 'activation')
    list_filter = ('promotion',)
    search_fields = ('promotion',)

class IndexPageAdminGroup(ModelAdminGroup):
    menu_label = 'Index Page'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (IndexPageAdmin, IndexImageAdmin)

modeladmin_register(IndexPageAdminGroup)
