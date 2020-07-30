from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Category, Genre, Title, Review, Comment, User


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Title
		fields = ['categoty', 'genre', 'name', 'year']


class ReviewSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
		slug_field='username',
		read_only=True
	)

	class Meta:
		model = Review
		fields = ('id', 'author', 'text', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
		slug_field='username',
		read_only=True
	)

	class Meta:
		model = Comment
		fields = ('id', 'author', 'text', 'pub_date')
