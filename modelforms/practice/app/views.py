from django.shortcuts import render
from app.forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def form_view(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request, 'app/form.html', {'form_html':form})
