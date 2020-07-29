from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import EmailConfirmationCode, UsersViewSet, Token

users_router_v1 = DefaultRouter()
users_router_v1.register('users', UsersViewSet)

urlpatterns = [
    path('', include(users_router_v1.urls)),
    path('auth/token/', Token.as_view(), name='token_obtain_pair'),
    path('auth/email/', EmailConfirmationCode.as_view(), name='email'),
]