from django import forms
from appTwo import models

class ModelFormUser(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
