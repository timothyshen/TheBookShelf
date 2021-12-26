import uuid

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .manager import CustomUserManager


# Create your models here.


class AuthUser(AbstractBaseUser, PermissionsMixin):
    """
    用户表，override了Django自己的用户表
    """
    # Fields tie to the roles!
    READER = 1
    AUTHOR = 2
    EDITOR = 3
    ADMIN = 4

    # Role choice
    ROLE_CHOICES = {
        (READER, u'Reader'),
        (AUTHOR, u'Author'),
        (EDITOR, u'Editor'),
        (ADMIN, u'Admin')
    }

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'
        db_table = "AuthUser"

    username_validator = UnicodeUsernameValidator()

    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4(), verbose_name='Public identifier')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=(("male", u"Male"), ("female", u"Female")),
                              default="Female",
                              max_length=150, verbose_name='Gender')
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    icon = models.ImageField(upload_to="media/image/%Y/%m",
                             default=u"media/image/default.png",
                             max_length=1000,
                             verbose_name=u"AuthUser icon", null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=1, verbose_name='Role')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'


    def __str__(self):
        return "{} - {}".format(self.email, self.username)

    def get_full_name(self):
        return self.email
