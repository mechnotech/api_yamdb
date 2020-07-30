from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import filters, viewsets

from .models import Category, Genre, Title, Review, Comment
from .serializers import CategorySerializer, GenreSerializer, TitleListSerializer, TitlePostSerializer, ReviewSerializer, CommentSerializer
from users.permissions import IsAdmin, IsOwnerOrReadOnly, IsModerator, IsOwner

from .models import Category, Genre, Title



class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdmin, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', '=year', '=genre__slug', '=category__slug']

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitlePostSerializer
#TODO:
''' что-то не так с фильтрами
   AssertionError: Проверьте, что при GET запросе `/api/v1/titles/` 
   фильтуется по `genre` параметру `slug` жанра '''


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly | IsAdmin | IsModerator]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        self.queryset = title.reviews.all()
        return self.queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        if Review.objects.filter(author=self.request.user, title=title).exists():
            raise ValidationError('Object exist!')
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly | IsAdmin | IsModerator]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        reviews = Review.objects.filter(title=title)
        review = get_object_or_404(reviews, pk=self.kwargs.get('review_id'))
        self.queryset = review.comments.all()
        return self.queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        reviews = Review.objects.filter(title=title)
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
