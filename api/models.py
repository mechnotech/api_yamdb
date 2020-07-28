from django.db import models
from pytils.translit import slugify


class BaseCatalog(models.Model):
	name = models.CharField(max_length=250, verbose_name='Название')
	slug = models.SlugField(verbose_name='SLUG', null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)


class Genre(BaseCatalog):

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'


class Category(BaseCatalog):

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Title(models.Model):
	name = models.CharField(max_length=250, verbose_name='Название')
	year = models.IntegerField(verbose_name='Год', null=True, blank=True)
	category = models.ForeignKey(
		Category,
		verbose_name='Категория',
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		related_name='titles')
	genre = models.ManyToManyField(
		Genre,
		blank=True,
		null=True,
		verbose_name='Жанры')

	def __str__(self):
		return f'{self.name} ({self.year}г.)'

	class Meta:
		#TODO: ХЗ как назвать правильно, переименовать потом
		verbose_name = 'Титл'
		verbose_name_plural = 'Титлы'
