from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),	#^--the beginning;\d--can only be a digit;+==need to be one or more digits;$--the end;example:http://127.0.0.1:8000/post/1233457/ is ok.
]