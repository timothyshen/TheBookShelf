from .models import Billing_address, Order, OrderItem
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)



class BillingAddressAdmin(ModelAdmin):
    model = Billing_address
    menu_label = 'Billing Adress'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('user',)
    list_filter = ('is_primary',)
    search_fields = ('user',)


class OrderAdmin(ModelAdmin):
    model = Order
    menu_label = 'Order'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('user',)
    list_filter = ('status',)
    search_fields = ('user',)


class PaymentGroup(ModelAdminGroup):
    menu_label = 'Payment'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BillingAddressAdmin, OrderAdmin)


modeladmin_register(PaymentGroup)
