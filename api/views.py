from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Category, Genre, Title, Review, Comment
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer, ReviewSerializer, CommentSerializer


class CategoriesViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewsViewSet(viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CommentsViewSet(viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CategorySerializer