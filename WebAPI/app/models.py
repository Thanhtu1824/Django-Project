from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Brand (models.Model):

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product (models.Model):

    name = models.CharField(max_length = 100)
    active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='all_products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='all_products')
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

