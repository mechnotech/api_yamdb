from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import (
    email_code, UsersViewSet,
    user_self_view, get_token, )

users_router_v1 = DefaultRouter()
users_router_v1.register('users', UsersViewSet)

urlpatterns = [
    path('v1/users/me/', user_self_view),
    path('v1/auth/token/', get_token, name='token'),
    path('v1/auth/email/', email_code, name='email'),
    path('v1/', include(users_router_v1.urls)),
]
