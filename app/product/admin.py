from .models import Top_up_item, Subscription_Plan, User_profile
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)


# Register your models here.

class TopUpAdmin(ModelAdmin):
    model = Top_up_item
    menu_label = 'Topup Item'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'price', 'book_coin', 'is_feature')
    list_filter = ('is_featured',)
    search_fields = ('price_id',)


class SubscriptionAdmin(ModelAdmin):
    model = Subscription_Plan
    menu_label = 'Topup Item'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'price', 'type', 'is_feature')
    list_filter = ('is_featured', 'type')
    search_fields = ('price_id',)


class UserProfileAdmin(ModelAdmin):
    model = User_profile
    menu_label = 'User Profile'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('user', 'balance', 'plan', 'plan_status')
    list_filter = ('plan_status', 'plan')
    search_fields = ('user', 'stripe_customer_id', 'stripe_subscription_id')


class ProductGroup(ModelAdminGroup):
    menu_label = 'Product'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (TopUpAdmin, SubscriptionAdmin, UserProfileAdmin)


modeladmin_register(ProductGroup)
