from django.db import models
from django.utils.translation import gettext as _

class ContactUs(models.Model):    
    first_name = models.CharField(_("first name"), max_length=100)
    
    last_name = models.CharField(_("last_name"), max_length=200)
    
    email = models.CharField(_("email"), max_length=100)
    
    message = models.TextField(_("message"))
    
    def __str__(self):
        return self.first_name

