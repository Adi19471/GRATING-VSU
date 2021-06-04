from django.db import models

# Create your models here.
class Register(models.Model):
    #gender = [('Male','Male'),('Female','Female'),('Others','Others')# ]
  

    name = models.CharField(max_length=100)

    mobile_no = models.CharField(max_length=10)

    age = models.IntegerField()

    email  = models.EmailField()

    adharDetailes = models.CharField(max_length=12)

    address = models.TextField()
    