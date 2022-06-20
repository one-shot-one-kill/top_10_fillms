from django.contrib import admin

from .models import Film, Tag, Country, Year


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
	list_display = ('title', )
	prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('tag', )
	prepopulated_fields = {'slug': ('tag', )}


@admin.register(Country)
class TagAdmin(admin.ModelAdmin):
	list_display = ('country', )
	prepopulated_fields = {'slug': ('country', )}


@admin.register(Year)
class TagAdmin(admin.ModelAdmin):
	list_display = ('year', )
	prepopulated_fields = {'slug': ('year', )}