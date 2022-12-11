from django.db import models
from email.mime import image
from pizzeria.settings import MEDIA_URL

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.pizza_name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topping_name

class Comments(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

