from django import forms
from app.models import UserData
from django.utils.translation import gettext_lazy as _

class TakeData(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'
        
