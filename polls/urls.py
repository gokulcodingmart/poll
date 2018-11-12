from django.conf.urls import  url
from . import views



urlpatterns = [
	url(r'^about/$', views.about, name='about' ),
	url(r'^contact/$', views.contact, name='contact' ),
	url(r'^details/(?P<id>\d+)/$', views.details, name='details' ),
	url(r'^create/$', views.create, name='create' ),
	url(r'^vote/(?P<id>\d+)/$', views.vote, name='vote' ),
	url(r'^tovote/$', views.tovote, name='tovote' ),
	# url(r'^like/$', views.like, name='like' ),




	url(r'^index/$', views.index, name='index' ),
   
   ]