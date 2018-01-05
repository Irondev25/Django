from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    myDict = { 'dynamic_insertion' : 'This is from the views.py' }
    return render(request, 'app/views.html', context=myDict)
