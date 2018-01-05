from django.shortcuts import render
from app import forms,models
# Create your views here.

def index(request):
    return render(request,'app/index.html')

def userDataView(request):
    data_list = models.UserData.objects.order_by('first_name')
    return render(request,'app/database.html',{'data_rec':data_list})

def formView(request):
    form = forms.TakeData()

    if request.method == 'POST':
        form = forms.TakeData(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'app/form.html',{'form':form})
