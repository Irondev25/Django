from django import forms

class SimpleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    #since CharField has Textinput as default but we need Textarea type input so widget is set to forms.Textarea
