from django.conf.urls import url
from app.views import formview, database

app_name = 'app'

urlpatterns = [
    url(r'^database/', database, name='database'),
    url(r'^form/', formview, name='form'),
]