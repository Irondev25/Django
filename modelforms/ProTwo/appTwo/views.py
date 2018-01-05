from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import ModelFormUser
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'apptwo/users.html',context=user_dict)

def form_page(request):
    form = ModelFormUser()

    if request.method == "POST":
        form = ModelFormUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request,'appTwo/form.html',{'form':form})
