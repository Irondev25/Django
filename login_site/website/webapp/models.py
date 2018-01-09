from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     #OneToOneField function is used because we want to create whole new table
     #and don't want to change django.contrib.auth.models.User
     #additional fields
     user_portfolio = models.CharField(max_length=150, blank=True)
     user_profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
