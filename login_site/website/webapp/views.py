from django.shortcuts import render
from webapp.forms import UserForm

# Create your views here.
def index(request):
    return  render(request, 'webapp/index.html')

def user_form_page(request):
    form =
