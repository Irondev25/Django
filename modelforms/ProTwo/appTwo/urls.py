from django.conf.urls import url
from appTwo import views
from appTwo import forms

urlpatterns = [
    url(r'^$',views.users,name='users'),
    url(r'^form/', forms.ModelFormUser, name='form')

]
