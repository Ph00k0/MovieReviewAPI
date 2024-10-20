from .models import Review, Movie
from .serializers import ReviewSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['title']

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MovieFilter
    ordering_fields = ['title', 'release_date']  # Add any other fields you want to sort by
    ordering = ['title']  # Default ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

# Assuming you already have ReviewViewSet as well
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['created_at', 'rating']
    ordering = ['-created_at']
    def get_queryset(self):
        """
        Restrict the returned reviews to only those that belong to the authenticated user.
        """
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the review with the logged-in user as the owner of the review.
        """
        movie_data = self.request.data.get('movie')
        movie_title = movie_data.get('title')

        # Check if the movie exists, if not, create it
        movie, created = Movie.objects.get_or_create(title=movie_title)
        serializer.save(user=self.request.user, movie=movie)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Allow updating of review only if the review belongs to the logged-in user.
        """
        review = self.get_object()
        if review.user != self.request.user:
            raise PermissionDenied("You cannot edit this review.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Allow deletion of review only if the review belongs to the logged-in user.
        """
        review = self.get_object()
        if review.user != self.request.user:
            raise PermissionDenied("You cannot delete this review.")
        instance.delete()

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle movie and review creation together.
        """
        try:
            movie_data = request.data.get('movie')
            movie_title = movie_data.get('title')

            # Create the movie if it doesn't exist
            movie, created = Movie.objects.get_or_create(title=movie_title)

            # Proceed with creating the review
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user, movie=movie)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": "Invalid movie data format. It should be a dictionary."}, status=status.HTTP_400_BAD_REQUEST)
