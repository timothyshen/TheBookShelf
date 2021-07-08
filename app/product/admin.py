from django.contrib import admin
from .models import Top_up_item, Subscription_Plan, User_profile

# Register your models here.


admin.site.register(Top_up_item)
admin.site.register(Subscription_Plan)
admin.site.register(User_profile)
