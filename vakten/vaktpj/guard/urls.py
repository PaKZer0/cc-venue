from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'^icecast/(?P<path>.*)$', views.IcecastProxyView.as_view(), name='icecast'),
]
