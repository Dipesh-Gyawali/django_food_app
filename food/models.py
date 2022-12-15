from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.CharField(max_length=400,default='https://dummyimage.com/640x360/fff/aaa')
    
    def __str__(self):
        return self.name