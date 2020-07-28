from django.contrib import admin
from .models import Title, Category, Genre


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('name',)
    empty_value_display = '-пусто-'


class TitlesAdmin(BaseAdmin):
    list_display = ('id', 'name', 'year', 'category')
    list_filter = ('year', 'category')


class CategoryAdmin(BaseAdmin):
    pass


class GenreAmdin(BaseAdmin):
    pass


admin.site.register(Genre, GenreAmdin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitlesAdmin)
