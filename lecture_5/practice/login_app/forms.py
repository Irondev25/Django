from django import forms
from .models import UserProfileModel
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.TextInput(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ('portfolio_site', 'profile_pic')