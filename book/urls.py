from django.conf.urls import patterns, url, include
from book import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
	url(r'^login/$', views.log_in, name='login'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^$', views.main_page_render, name='main_page_render'),
	url(r'^submit/', views.submit, name='submit'),
	url(r'^/delete$', views.remove, name='delete'),
	url(r'^/edit$', views.edit, name='edit'),
	url(r'^make_csv/$', views.make_csv, name='make_csv'),
)