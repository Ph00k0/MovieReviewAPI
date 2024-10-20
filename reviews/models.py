from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)  # Overall movie rating
    release_date = models.DateField(default=datetime.date.today)  

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(default="1")
    rating = models.IntegerField()  # Rating should be between 1 and 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"

    def clean(self):
        # Ensure rating is within the desired range
        if not 1 <= self.rating <= 5:
            raise ValidationError('Rating must be between 1 and 5.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Call clean method to validate the rating before saving
        super().save(*args, **kwargs)
