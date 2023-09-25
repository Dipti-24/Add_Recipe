from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

class Car(models.Model):
    brand=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.brand