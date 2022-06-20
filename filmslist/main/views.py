from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count

from .models import Film, Comment
from .forms import CommentForm


def main(request):
	obj_list = Film.objects.all()
	paginator = Paginator(obj_list, 2)
	page = request.GET.get('page')
	try:
		films = paginator.page(page)
	except PageNotAnInteger:
		films = paginator.page(1)
	except EmptyPage:
		films = paginator.page(paginator.num_pages)
	return render(request, 'main/pages/home.html', {'page': page, 'films': films})


def filter_year(request, year):
	obj_list = Film.objects.filter(created_year__year=year)
	return render(request, 'main/pages/home.html', {'films': obj_list})
	# films/year/{{ film.created_year }}


def filter_country(request, country):
	obj_list = Film.objects.filter(country__country=country)
	return render(request, 'main/pages/home.html', {'films': obj_list})
	#films/country/{{ name.country }}


def filter_tag(request, tag):
	obj_list = Film.objects.filter(tags__tag=tag)
	return render(request, 'main/pages/home.html', {'films': obj_list})


def detail(request, film):
	film = get_object_or_404(Film, slug=film)
	comments = film.comments.filter(active=True)
	comment_form = None 
	new_comment = None 
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.film = film 
			new_comment.save()
		else:
			comment_form = CommentForm()
	film_tags_ids = film.tags.values_list('id', flat=True)
	similar_posts = Film.objects.filter(tags__in=film_tags_ids).exclude(id=film.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags')[:4]
	return render(request, 'main/pages/detail.html', {'film': film, 'comments': comments,
		'comment_form': comment_form, 'new_comment': new_comment, 'similar_posts': similar_posts})