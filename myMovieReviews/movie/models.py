from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    runtime = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title