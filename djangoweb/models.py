from django.db import models

# Create your models here.

class Users(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class Customer(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField(null=True,blank=True)
    pol = models.FloatField(null=True,blank=True)
    sub = models.FloatField(null=True,blank=True)
    link = models.CharField(max_length=200,default="https://en.wikipedia.org/wiki/Emirates_(airline)",null=True,blank=True)