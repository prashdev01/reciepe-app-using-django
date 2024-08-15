from django.db import models

# Create your models here.
class  students(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    address  = models.TextField(null=True,blank=True)
    
    
class Car(models.Model):
    car_name = models.CharField( max_length=500)
    car_speed = models.IntegerField()
    
    def __str__(self):
        return self.car_name
    