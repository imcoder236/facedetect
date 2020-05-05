from django.db import models
from django.contrib.auth.models import User
#from rest_framework import serializers
# Create your models here.
class uploadImage(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'images/')
    email = models.CharField(max_length = 50,null=True)
    gender = models.CharField(max_length = 50,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length = 50,null=True)
    pincode = models.CharField(max_length = 50,null=True)
    aadharno = models.CharField(max_length = 50,null=True)
    phone = models.CharField(max_length = 50,null=True)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class location(models.Model):
    area = models.CharField(max_length = 50)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class ip_address(models.Model):
    area = models.CharField(max_length = 50)
    ip = models.CharField(max_length = 50)
    port = models.CharField(max_length = 50)
    strs = models.CharField(max_length = 50)
    status=models.PositiveSmallIntegerField(default=0)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class live_track_record(models.Model):
    name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)
    ip = models.CharField(max_length = 50)
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(uploadImage, on_delete=models.CASCADE, null=True)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class users(models.Model):
    name = models.CharField(max_length = 50,null=True)
    email = models.CharField(max_length = 50,null=True)
    passwd = models.CharField(max_length = 50,null=True)
    phoneno = models.CharField(max_length = 50,null=True)
    creat_time = models.DateTimeField(auto_now_add=True,null=True)
    status = models.PositiveSmallIntegerField(default=1)
#     dob = models.DateField(null=True)
#     address = models.CharField(max_length = 50,null=True)
#     city = models.CharField(max_length = 50,null=True)
#     state = models.CharField(max_length = 50,null=True)
#     pincode = models.CharField(max_length = 50,null=True)
#     aadharno = models.CharField(max_length = 50,null=True)
#     phone = models.CharField(max_length = 50,null=True)
#     def delete(self, *args, **kwargs):
#         super().delete(*args, **kwargs)

class ip_status_report(models.Model):
    ipadd = models.CharField(max_length = 50,null=True)
    in_time = models.DateTimeField(auto_now_add=True,null=True)
    out_time = models.DateTimeField(null=True)
    status = models.PositiveSmallIntegerField(default=1)

class users_report(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    in_time = models.DateTimeField(null=True)
    out_time = models.DateTimeField(null=True)
    # status = models.CharField(max_length = 50,null=True)

class state(models.Model):
    state_n = models.CharField(max_length = 50,null=True)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class city(models.Model):
    city_n = models.CharField(max_length = 50,null=True)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE,null=True)
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class passwd(models.Model):
    user_id = models.CharField(max_length = 50,null=True)
    username = models.CharField(max_length = 50,null=True)
    umail = models.CharField(max_length = 50,null=True)
    date = models.DateTimeField(null=True)
