# reviews/models.py

from django.db import models

class MovieReview(models.Model):
    title = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title


# Create your models here.
