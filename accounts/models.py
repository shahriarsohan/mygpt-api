from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from .managers import UserManager


class Accounts(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,
                              unique=True, db_index=True)
    is_staff = models.BooleanField(
        default=False, help_text=(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(default=True, help_text=(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    username = models.CharField(max_length=50, blank=True, null=True)
    license_key = models.CharField(max_length=255, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:  # noqa: D101
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email
