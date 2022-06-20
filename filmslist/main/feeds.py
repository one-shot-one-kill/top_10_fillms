from django.contrib.syndication.views import Feed 
from django.template.defaultfilters import truncatewords

from .models import Film 


class LatestFilmFeed(Feed):
	title = 'Film list'
	link = '/filmlist/'
	description = 'Top 10 films ever'

	def items(self): 
		return Film.objects.all()

	def item_title(self, item):
		return item.title 

	def item_description(self, item):
		return truncatewords(item.description, 30)