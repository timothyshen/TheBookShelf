from django.db import models

from user.models import AuthUser


class Top_up_item(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    book_coin = models.IntegerField(default=0)
    monthly_ticket_number = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    num_available = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title


class Subscription_Plan(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    num_available = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title


class User_profile(models.Model):
    PLAN_ACTIVE = 'VIP'
    PLAN_INACTIVE = 'normal'

    CHOICES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'VIP'),
        (PLAN_INACTIVE, 'Normal')
    )
    user = models.OneToOneField(AuthUser, related_name='created_profile', on_delete=models.CASCADE)
    Balance = models.IntegerField(default=0)
    plan = models.ForeignKey(Subscription_Plan, related_name='vip_status', on_delete=models.SET_NULL, null=True,
                             blank=True)
    plan_status = models.CharField(max_length=20, choices=CHOICES_PLAN_STATUS, default=PLAN_INACTIVE)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'VIP for {}'.format(self.user)
