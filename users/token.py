from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class YamTokenSerializer(TokenObtainPairSerializer):
    # username_field = User.email

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.HiddenField()
        self.fields['password'] = serializers.HiddenField()
        self.fields['email'] = serializers.CharField()
        self.fields['confirm_code'] = serializers.CharField()

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token


class YamTokenObtainPairView(TokenObtainPairView):
    serializer_class = YamTokenSerializer
