# -*- coding: utf-8 -*-
__author__ = 'ffuentes'

from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the venue index.")

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
