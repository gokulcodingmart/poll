from django.conf.urls import  url
from . import views



urlpatterns = [
	# url(r'^about/$', views.about, name='about' ),
	# url(r'^contact/$', views.contact, name='contact' ),
	# url(r'^business/$', views.business, name='business' ),
	# url(r'^education/$', views.education, name='education' ),
	# url(r'^comment/(?P<id>\d+)/$', views.comment, name='comment' ),
	# url(r'^ajaxcomment/$', views.ajaxcomment, name='ajaxcomment' ),
	# url(r'^like/$', views.like, name='like' ),




	url(r'^index/$', views.index, name='index' ),
   
   ]