# movies/models.py
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image_url = models.URLField()# Add the library field
    available = models.BooleanField(default=True)

    rented_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def is_rented(self):
        return self.rented_by is not None

class Rental(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now_add=True)



