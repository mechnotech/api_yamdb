from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet

router = DefaultRouter()

router.register('categories', CategoriesViewSet, basename='categories')

# urlpatterns = [
#     path('v1/', include('users.urls')),
# ]

urlpatterns = [
    path('v1/', include(router.urls))
]
