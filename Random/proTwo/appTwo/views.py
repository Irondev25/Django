from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>Second App</em>')

def help_page(request):
    return render(request,'help.html')

def user_page(request):
    return 
