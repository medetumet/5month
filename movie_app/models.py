from django.db import models

# Create your models here.

class Director(models.Model):
    name=models.CharField(max_length=250)

class Movie(models.Model):
    title=models.CharField(max_length=204)
    description=models.TextField(max_length=400)
    duration=models.FloatField()
    director=models.ForeignKey(Director,on_delete=models.CASCADE)

RATING = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)

class Review(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=RATING)





