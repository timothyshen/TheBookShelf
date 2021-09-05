# Register your models here.
from .models import Comment
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)


class CommentAdmin(ModelAdmin):
    model = Comment
    menu_label = 'Comment'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('user', 'book')
    list_filter = ('created_on',)
    search_fields = ('user', 'book')


modeladmin_register(CommentAdmin)
