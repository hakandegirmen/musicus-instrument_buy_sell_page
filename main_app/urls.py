from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index')
]

if settings.DEBUG: 
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, 
		{'document_root': settings.MEDIA_ROOT,}),
	]