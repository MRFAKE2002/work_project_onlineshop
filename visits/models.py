from django.db import models
from django.utils.translation import gettext as _

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(_('IP address'), )




