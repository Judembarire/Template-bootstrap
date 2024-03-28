from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    subject = models.CharField(max_length=20)


