#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '02/06/2021 23:42'

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not username:
            raise ValueError(_("The username must be set"))
        if not password:
            raise ValueError(_("The password must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 4)

        if extra_fields.get('role') != 1:
            raise ValueError("Superuser must be admin!")
        return self.create_user(email, username, password, **extra_fields)
