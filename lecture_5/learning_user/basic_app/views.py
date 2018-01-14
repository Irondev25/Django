from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            print(profile)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{
                                                           'registered':registered,
                                                           'user_form':user_form,
                                                           'profile_form':profile_form ,
                                                        })
            