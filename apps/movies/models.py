from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=255)
    release_date = models.DateField()
    planets = models.ManyToManyField('planets.Planet', related_name='movies')
