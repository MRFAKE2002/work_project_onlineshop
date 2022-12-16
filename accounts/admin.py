from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    FORM = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'email',]