#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '02/06/2021 23:42'

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    override Django内置表需要重新编写userManager
    """

    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **extra_fields):
        """
        创建超级用户（superuser）
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('role', 4)

        if extra_fields.get('role') != 4:
            raise ValueError("Superuser must be admin!")
        return self.create_user(self, email, username, first_name, password, **extra_fields)
