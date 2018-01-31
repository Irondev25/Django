from django.shortcuts import render
from .forms import UserInfoForm, UserProfileInfoForm

#All the shit for login 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index_view(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_view(request):
    registered = False

    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserInfoForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form' : user_form,
                                                           'profile_form' : profile_form,
                                                           'registered' : registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('https://www.google.com'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to log in and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login Details supplied")
    else:
        return render(request, 'basic_app/login.html')