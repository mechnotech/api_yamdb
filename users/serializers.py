from rest_framework import serializers

from users.models import YamUser


class YamUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = YamUser
        fields = (
            "first_name", "last_name",
            "username", "bio", "email", "role")
