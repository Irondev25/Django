from django.shortcuts import render
from .forms import UserInfoForm, UserProfileInfoForm
# Create your views here.
def index_view(request):
    return render(request, 'basic_app/index.html')

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
