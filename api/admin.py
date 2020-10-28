from django.contrib import admin

from .models import Review, Comment, Title, Genre, Category

class GengeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    empty_value_display = '-пусто-'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    empty_value_display = '-пусто-'

class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description')
    empty_value_display = '-пусто-'

class RewiewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text', 'pub_date', 'score')
    search_fields = ('text',)
    list_filter = ('pub_date', 'score',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'author', 'text', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author',)
    empty_value_display = '-пусто-'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GengeAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, RewiewAdmin)
admin.site.register(Comment, CommentAdmin)