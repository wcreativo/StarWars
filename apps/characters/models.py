from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    movies = models.ManyToManyField('movies.Movie', related_name='characters')
