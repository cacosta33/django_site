from django.shortcuts import render


#Create your views here

def index(request):
	return render(request, 'home/index.html')

def about_me(request):
	return render(request, 'home/about_me.html')

def bad_request(request):
	return render(request, "home/error_pages/404.html")
