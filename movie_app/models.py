from django.db import models

# Create your models here.

class Director(models.Model):
    name=models.CharField(max_length=250)

class Movie(models.Model):
    title=models.CharField(max_length=204)
    description=models.TextField(max_length=400)
    duration=models.FloatField()
    director=models.ForeignKey(Director,on_delete=models.CASCADE)

class Review(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)


