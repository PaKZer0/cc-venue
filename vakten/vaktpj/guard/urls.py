# -*- coding: utf-8 -*-
__author__ = 'ffuentes'

from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='index'),
]
