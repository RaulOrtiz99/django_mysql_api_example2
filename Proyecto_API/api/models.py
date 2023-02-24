from django.db import models

# Create your models here.

#este es el modelo de datos para la bd

class Company(models.Model):
    name = models.CharField(max_length=200)
    website= models.URLField(max_length=200)
    foundation= models.PositiveBigIntegerField()

