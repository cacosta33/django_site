from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),

	#ex /about_me
	url(r'^about_me/$', views.about_me, name='about_me'),


]