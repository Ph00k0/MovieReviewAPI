# reviews/serializers.py
from rest_framework import serializers
from .models import Review, Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'rating', 'release_date']

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()  # Nested MovieSerializer to handle movie data

    class Meta:
        model = Review
        fields = ['id', 'movie', 'review_text', 'rating', 'created_at']

    def create(self, validated_data):
        movie_data = validated_data.pop('movie')
        movie, created = Movie.objects.get_or_create(**movie_data)
        review = Review.objects.create(movie=movie, **validated_data)
        return review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
