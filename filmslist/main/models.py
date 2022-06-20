from django.db import models
from django.urls import reverse


class Year(models.Model):
	year = models.IntegerField(default=0)
	slug = models.SlugField(max_length=5)

	def __str__(self):
		return str(self.year) 


class Country(models.Model):
	country = models.CharField(max_length=20)
	slug = models.SlugField(max_length=20)

	def __str__(self):
		return self.country 


class Tag(models.Model):
	tag = models.CharField(max_length=20)
	slug = models.SlugField(max_length=20)

	def __str__(self):
		return self.tag


class Film(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	created_year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, related_name='created_year')
	country = models.ManyToManyField(Country, related_name='created_country')
	tags = models.ManyToManyField(Tag, related_name='tags')
	description = models.TextField()
	image = models.ImageField(upload_to='images')

	def get_absolute_url(self):
		return reverse('detail', args=[self.slug])


class Comment(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)