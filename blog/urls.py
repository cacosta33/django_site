from django.conf.urls import url

from . import views

urlpatterns = [

	#ex: /blog/
	url(r'^$', views.index, name='index'),

	#ex: /blog/view
	url(r'^blog/view(?P<slug>[^\.]+)/$', views.view_post, name='blog_post'),

	#ex /blog/category
	url(r'^blog/category(?P<slug>[^\.]+)/$', views.view_category, name='blog_category'),




]