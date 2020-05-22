from django.db import models
<<<<<<< HEAD
from accounts.models import User
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_images',blank=True)
    add_ons = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name


class Restaurant(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to='restaurant_images',blank=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("main:homepage")
=======

# Create your models here.
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
