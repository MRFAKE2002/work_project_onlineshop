
from django.contrib.auth.tokens import  PasswordResetTokenGenerator
from django.utils import six

from .models import CustomUser

class TokenGenerator(PasswordResetTokenGenerator):
    
    def _make_hash_value(self, user: CustomUser, timestamp: int) -> str:
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)

account_activation_token = TokenGenerator()
