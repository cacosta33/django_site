from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),

	#ex: /about_me
	url(r'^about_me/$', views.about_me, name='about_me'),

	#ex: /resume
	url(r'^resume/$', views.resume, name='resume'),

	#ex: /contact
	url(r'^contact/$', views.contact, name='contact'),

]