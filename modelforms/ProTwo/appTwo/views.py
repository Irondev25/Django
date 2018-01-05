from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import ModelFormUser
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def database(request):
    data_list = User.objects.all()
    return render(request,'appTwo/users.html',{'data_rec':data_list})


def users(request):
    form = ModelFormUser()

    if request.method == "POST":
        form = ModelFormUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request,'appTwo/form.html',{'form':form})
