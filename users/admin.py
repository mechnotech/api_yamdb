from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import YamUserCreationForm, YamUserChangeForm
from .models import YamUser


class YamUserAdmin(UserAdmin):
    add_form = YamUserCreationForm
    form = YamUserChangeForm
    model = YamUser
    list_display = ('username', 'email',)


admin.site.register(YamUser, YamUserAdmin)
