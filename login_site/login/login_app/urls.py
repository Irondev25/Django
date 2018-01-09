from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path(r'^register/', views.register ,name='register'),
]
