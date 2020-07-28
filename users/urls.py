from django.urls import path

from users.views import Token

urlpatterns = [
    # path('auth/token/', YamTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/', Token.as_view(), name='token_obtain_pair'),
]
