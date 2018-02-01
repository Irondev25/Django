from django.conf.urls import url
from login_app import views

#app_name(relative Url)
app_name = 'login_app'

urlpatterns = [
    url(r'^registration/$', views.registration_view, name='registration'),
]