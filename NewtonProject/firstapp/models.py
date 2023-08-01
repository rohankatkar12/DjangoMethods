from django.db import models


class College(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=15, default=None)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    email = models.EmailField()
    address = models.TextField()
    contact = models.CharField(max_length=15, default=None)

    def __str__(self):
        return self.name  


class Car(models.Model):
    car_name = models.CharField(max_length=100) 
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name