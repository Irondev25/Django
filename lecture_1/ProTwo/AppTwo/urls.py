from django.conf.urls import url
from AppTwo import views

urlpatterns = [

    url(r'^index/', views.index, name='index'),
    url(r'^help/', views.help, name='help')
]
