from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .form import ContactForm
#Create your views here

def index(request):
	return render(request, 'home/index.html')

def about_me(request):
	return render(request, 'home/about_me.html')

def bad_request(request):
	return render(request, "home/error_pages/404.html")

def resume(request):
	with open('home/static/home/images/CesarAcostaResume.pdf', 'r') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'filename=cesar_acosta_resume.pdf'
		return response
	pdf.closed

def contact(request):	
	# If this is a POST request we need to process the form data
	if request.method == 'POST':
		#Create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			return HttpResponseRedirect('home:index')
	else:
		form = ContactForm()

	return render(request, 'home/contact.html', {'form': form})