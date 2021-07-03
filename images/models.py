from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='articles/')
    name = models.CharField(max_length=55)
    author =models.CharField(max_length=255,default='Admin')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)