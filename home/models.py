from django.db import models
from django.db.models import CharField


# Create your models here.
class Student(models.Model):
    # Id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def setName(self, studentName):
        self.name = studentName


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> CharField:
        return self.car_name
