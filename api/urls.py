from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet

users_router_v1 = DefaultRouter()

users_router_v1.register('categories', CategoriesViewSet, basename='categories')

# urlpatterns = [
#     path('v1/', include('users.urls')),
# ]

urlpatterns = [
    path('v1/', include(users_router_v1.urls))
]
