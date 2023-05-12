from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text="Email address")
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')