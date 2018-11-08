from django.conf.urls import  url
from . import views



urlpatterns = [
	url(r'^about/$', views.about, name='about' ),
	url(r'^contact/$', views.contact, name='contact' ),
	url(r'^details/(?P<id>\d+)/$', views.details, name='details' ),
	# url(r'^education/$', views.education, name='education' ),
	url(r'^vote/(?P<id>\d+)/$', views.vote, name='vote' ),
	# url(r'^ajaxcomment/$', views.ajaxcomment, name='ajaxcomment' ),
	# url(r'^like/$', views.like, name='like' ),




	url(r'^index/$', views.index, name='index' ),
   
   ]