from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")
