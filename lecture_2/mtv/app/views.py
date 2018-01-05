from django.shortcuts import render
from app.models import User

# Create your views here.
def data(request):
    data_list = User.objects.order_by('first_name')
    data_dict = {'data_record':data_list}
    return render(request, 'app/data.html', context=data_dict)
