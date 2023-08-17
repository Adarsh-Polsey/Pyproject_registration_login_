from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)
class reg(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class complaint(models.Model):
    complaint=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    REGISTRATION=models.ForeignKey(reg,on_delete=models.CASCADE)