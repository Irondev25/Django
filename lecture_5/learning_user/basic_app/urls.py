from django.urls import path
from basic_app import views

#Tempate Urls!!
app_name = 'basic_app'

urlpatterns=[
    path('register/', views.registration, name='register'),
]