from rest_framework import serializers

from .models import Category, Genre, Title, Review, Comment


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
	class Meta:
		model = Review
		fields = ['title', 'author', 'text', 'score', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['review', 'author', 'text', 'pub_date']
