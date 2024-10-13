# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    usertype = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'input'}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'usertype', 'password1', 'password2')  # Ensure these are correct
