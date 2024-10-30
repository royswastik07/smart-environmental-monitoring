# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True, widget=forms.Select(attrs={'class': 'input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'dob', 'gender', 'first_name', 'last_name', 'password1', 'password2')
