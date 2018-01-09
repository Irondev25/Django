from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = UserProfileInfo
        fields = ('username','email','password','portfolio','profile_pic')
