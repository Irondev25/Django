from django import forms
from app.models import UserData

class TakeData(forms.ModelForm):
    class Meta():
        model = UserData
        fields = '__all__'
        
