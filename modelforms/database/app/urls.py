from django.conf.urls import url
from app.views import formView,userDataView

app_name = 'app'

urlpatterns = [
    url(r'^data/', userDataView, name='database'),
    url(r'^form/', formView, name='form')
]
