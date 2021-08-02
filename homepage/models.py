from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.ImageField(upload_to='productimages',null = True)
    descrition = models.TextField(max_length=2500)
    Medium_price = models.FloatField(null=True)
    Large_price = models.FloatField(null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=50000)
    email = models.CharField(max_length=200)
    Contact_No = models.IntegerField(max_length=12)

    def __str__(self):
        return self.name

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField(max_length=100)

    def __str__(self):
        return self.username


