from django.db import models

# Create your models here.



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField()
    views = models.IntegerField(null=True)

class Comments(models.Model):
    time = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
