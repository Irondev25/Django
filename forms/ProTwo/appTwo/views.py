from django.shortcuts import render
from appTwo.form import NewUserForm
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request,'appTwo/users.html',{'form':form})
