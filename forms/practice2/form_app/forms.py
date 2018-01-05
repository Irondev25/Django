from django import forms

class FormName(forms.Form):
    name = forms.CharField(help_text='Name')
    email = forms.EmailField(help_text='Email Address')
    text = forms.CharField(help_text='Message',widget=forms.Textarea)

    def clean(self): #evoked only when submit button is pressed
        cleaned_data = super().clean() #returns a dict {'name': 'amit', 'email': 'amit@gmail.com', 'text': 'hello'}
        name = cleaned_data['name']
        if name[0].lower() == 'a':
            raise forms.ValidationError("Dont start with a")
