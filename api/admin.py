from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


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

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text', 'pub_date', 'score')
    search_fields = ('text',)
    list_filter = ('pub_date', 'score',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'author', 'text', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre, GenreAmdin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitlesAdmin)
