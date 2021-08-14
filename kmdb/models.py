from django.db import models
from django.contrib.auth.models import User

# -----------------------------------------


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    duration = models.CharField(max_length=255)
    premiere = models.CharField(max_length=255)
    classification = models.IntegerField()
    synopsis = models.CharField(max_length=255)

    class Meta:
        db_table = "movies"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    movies = models.ManyToManyField(Movie, related_name="genres")

    class Meta:
        db_table = "genres"


class Review(models.Model):
    stars = models.IntegerField()
    review = models.CharField(max_length=255)
    spoilers = models.BooleanField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    critic = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    class Meta:
        db_table = "reviews"
