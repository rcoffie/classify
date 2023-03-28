from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ['-created_on']
        
      
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField() 
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # In future set image path and default image
    Image = models.ImageField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['name','price','category'])]


    def __str__(self):
        return self.name 

