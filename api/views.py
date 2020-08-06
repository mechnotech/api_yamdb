from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Avg, ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.exceptions import NotAcceptable, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api.filters import TitleFilter
from api.models import Category, Genre, Review, Title
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleListSerializer, TitlePostSerializer,
                             YamUsersSerializer)
from api_yamdb import settings
from users.models import YamUser
from users.permissions import IsAdminOrStaff, IsModerator, IsOwner, ReadOnly


class CatalogViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    permission_classes = [IsAdminOrStaff | ReadOnly]
    lookup_field = 'slug'
    search_fields = ['=name']
    filter_backends = [filters.SearchFilter]


class CategoriesViewSet(CatalogViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenresViewSet(CatalogViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    permission_classes = [IsAdminOrStaff | ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitlePostSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated | ReadOnly, IsOwner | ReadOnly |
                          IsAdminOrStaff | IsModerator]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        self.queryset = title.reviews.all()
        return self.queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        if Review.objects.filter(author=self.request.user,
                                 title=title).exists():
            raise ValidationError('Object exist!')
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated | ReadOnly, IsOwner | ReadOnly |
                          IsAdminOrStaff | IsModerator]

    def get_queryset(self):
        comments = get_object_or_404(
            Review.objects.filter(title_id=self.kwargs.get('title_id')),
            pk=self.kwargs.get('review_id')
        ).comments.all()
        self.queryset = comments
        return self.queryset

    def perform_create(self, serializer):

        review = get_object_or_404(
            Review.objects.filter(title_id=self.kwargs.get('title_id')),
            pk=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrStaff,)
    queryset = YamUser.objects.all()
    serializer_class = YamUsersSerializer
    lookup_field = 'username'

    @action(detail=False, methods=('GET', 'PATCH'),
            permission_classes=(IsAuthenticated,))
    def me(self, request):
        user = get_object_or_404(YamUser, id=request.user.id)

        if request.method == 'GET':
            serializer = YamUsersSerializer(user)
            return Response(serializer.data)

        if request.method == 'PATCH':
            serializer = YamUsersSerializer(user,
                                            data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def email_code(request):
    data = {
        'email': request.data.get('email'),
        'username': f'newuser_{YamUser.objects.count()}',
    }

    serializer = YamUsersSerializer(data=data)

    if serializer.is_valid():
        user = serializer.save()
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject=settings.MAIL_SUBJECT,
            message=f'{settings.MAIL_TEXT}{confirmation_code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=(data['email'],),
            fail_silently=False,
        )
        return Response({serializer.data['email']},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def get_token(request):
    email = request.data['email']
    confirmation_code = request.data['confirmation_code']

    try:
        user = YamUser.objects.get(email=email)
    except ObjectDoesNotExist:
        raise NotAcceptable(detail='No such e-mail')

    if default_token_generator.check_token(user, confirmation_code):
        refresh = RefreshToken.for_user(user)
        return Response(data={'token': str(refresh.access_token)},
                        status=status.HTTP_200_OK)

    raise NotAcceptable(detail='error code')
