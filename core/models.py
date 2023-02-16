from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.utils.translation import gettext_lazy as _
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class Group(BaseGroup):
    def __str__(self) -> str:
        return self.name
