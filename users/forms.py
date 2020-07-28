from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import YamUser


class YamUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = YamUser
        fields = ('username', 'email', 'bio')


class YamUserChangeForm(UserChangeForm):

    class Meta:
        model = YamUser
        fields = ('username', 'email', 'bio')
