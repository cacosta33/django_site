from django.conf.urls import url

from . import views

urlpatterns = [
	#ex: /pokemon/
	url(r'^$', views.index, name='index'),

	#ex: /pokemon/157
	url(r'^(?P<pokedex_number>[0-9]+)/$', views.details, name='details')

	
]
