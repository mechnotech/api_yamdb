from rest_framework import serializers

from users.models import YamUser


class YamRegUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = YamUser
        fields = ['email']
