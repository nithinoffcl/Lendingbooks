from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    collegename = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=1500)
    password = models.CharField(max_length=32)
    retypepassword = models.CharField(max_length=32,default = 'DEFAULT VALUE')

class Order(models.Model):
    no = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=1500, default = 'DEFAULT VALUE')

class Login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=32)
