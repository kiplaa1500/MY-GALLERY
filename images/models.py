from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location_name=models.CharField(max_length=255)
    
    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.location_name
    
    
class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def save_category(self):
        self.save()
    
    def __str__(self):
        return self.name
class Image(models.Model):
    image = models.ImageField(upload_to='articles/')
    name = models.CharField(max_length=55)
    author =models.CharField(max_length=255,default='Admin')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)

    
    def save_image(self):
        self.save()
    
    def __str__(self):
        return self.image
    class Meta:
        ordering = ['image']
        
        

    