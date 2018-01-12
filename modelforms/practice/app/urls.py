from django.contrib import admin
from django.urls import path, include
from app.views import form_view

app_name = 'app'

urlpatterns = [
    path('form/', form_view, name='form')
]
