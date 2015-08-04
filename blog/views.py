from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.

def index(request):
	context = { 
		'categories': Category.objects.all(),
		'posts': Blog.objects.all()[:5],
	}
	return render(request, 'blog/index.html', context)

def view_post(request, slug):
	context = { 'post': get_object_or_404(Blog, slug=slug) }
	return render(request, 'blog/view_post.html', context)

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = { 'category': category,
				'posts': Blog.objects.filter(category=category)[:5] 
			}
	return render(request, 'blog/view_category.html', context)