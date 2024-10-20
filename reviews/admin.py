# reviews/admin.py

from django.contrib import admin
from .models import Movie, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # Number of empty forms to display

class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)



# Register your models here.
