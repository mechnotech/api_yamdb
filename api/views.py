from django.db.models import Avg
from rest_framework import filters, viewsets

from users.permissions import IsAdmin, IsOwnerOrReadOnly, IsSelfOrAdmin

from .models import Category, Genre, Title
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleListSerializer, TitlePostSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSelfOrAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSelfOrAdmin, IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', '=year', '=genre__slug', '=category__slug']

    def get_serializer_class(self):
        if self.action in ('list',):
            return TitleListSerializer
        return TitlePostSerializer
#TODO:
''' что-то не так с фильтрами
   AssertionError: Проверьте, что при GET запросе `/api/v1/titles/` 
   фильтуется по `genre` параметру `slug` жанра '''
