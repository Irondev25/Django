from django.conf.urls import url
from app.views import other,relative

app_name = 'app'

urlpatterns = [
    url(r'^relative/',relative,name='relative'),
    url(r'^other/',other,name='other')
]
