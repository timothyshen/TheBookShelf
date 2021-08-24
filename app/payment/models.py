import uuid as uuid
from django.db import models
from user.models import AuthUser
from product.models import Top_up_item, User_profile, Subscription_Plan


# Create your models here.

class Billing_address(models.Model):
    user = models.ForeignKey(AuthUser, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_primary:
            try:
                temp = Billing_address.objects.get(is_primary=True)
                if self != temp:
                    temp.is_primary = False
                    temp.save()
            except Billing_address.DoesNotExist:
                print('did not set a primary adress')
                pass
        super(Billing_address, self).save(*args, **kwargs)


class Order(models.Model):
    ORDERED = 'unpaid'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (ORDERED, 'unpaid'),
        (COMPLETED, 'completed'),
        (CANCELLED, 'Cancelled'),
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(AuthUser, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(Billing_address, related_name='orders', on_delete=models.SET_NULL, blank=True,
                                        null=True)
    product_name = models.CharField(default='', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    used_coupon = models.CharField(max_length=50, blank=True, null=True)

    payment_intent = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def __str__(self):
        return '%s' % self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    topup = models.ForeignKey(Top_up_item, related_name='topup', on_delete=models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(Subscription_Plan, related_name='plan', on_delete=models.DO_NOTHING, blank=True, null=True)
    vip_account = models.ForeignKey(User_profile, related_name='vip_account', on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return '%s' % self.id
