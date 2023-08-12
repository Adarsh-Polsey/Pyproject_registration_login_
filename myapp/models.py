from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class reg(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cnfrm_pswd=models.CharField(max_length=100)