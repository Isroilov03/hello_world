from django.db import models

# Create your models here.

class Brend(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class Mashina(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teacher_photo')
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    price = models.IntegerField()
    brand = models.ForeignKey(Brend, on_delete=models.CASCADE)

class Avtosalon(models.Model):
    nomi = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    boshlash = models.TimeField()
    tugash = models.TimeField()
