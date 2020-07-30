from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet, CommentsViewSet, ReviewsViewSet

users_router_v1 = DefaultRouter()

users_router_v1.register('categories', CategoriesViewSet, basename='categories')

users_router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
users_router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
# urlpatterns = [
#     path('v1/', include('users.urls')),
# ]

urlpatterns = [
    path('v1/', include(users_router_v1.urls))
]
