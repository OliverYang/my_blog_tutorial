from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


# Create your models here.

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Illegal email format!')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_superuser=is_superuser, last_login=timezone.now(),
                          create_date=timezone.now(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_normal_user(self, email, password=None, **extra_fields):
        return self.create_user(self, email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(self, email, password, True, **extra_fields)


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('Email Address'), help_text=_('Your email address here'), max_length=254, unique=True,
                              db_index=True)
    nickname = models.CharField(_('Nickname'), help_text=_('Your nickname here'), max_length=30, blank=True)
    is_active = models.BooleanField(_('Active'), help_text=_('Active or not'), default=True)
    create_date = models.DateTimeField(_('Create Date'), help_text=_('User account create date'),
                                       default=timezone.now())

    def get_username(self):
        return self.nickname

    def user_status(self):
        return self.is_active

    @property
    def favourite(self):
        pass

    def add_favourite(self):
        pass

    def removo_favoutite(self):
        pass
