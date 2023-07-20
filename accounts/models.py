from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    # phone_number = models.CharField(_("phone_number"), max_length=11, unique=True, null=False, blank=False, help_text=_("like 09123456789"))
    phone_number = PhoneNumberField()
    city = models.CharField(_("city"), max_length=100, null=False, blank=False, help_text=_("like Tehran"))

