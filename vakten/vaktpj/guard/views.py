from django.http import HttpResponse
from django.shortcuts import render
from revproxy.views import ProxyView

import os

def index(request):
    return HttpResponse("Hello, world. You're at the venue index.")

class IcecastProxyView(ProxyView):
    upstream = 'http://{}:{}/'.format(
		os.getenv('ICECAST_SERVER_NAME', 'cc-venue_icecast_1'),
		os.getenv('ICECAST_SERVER_PORT', '8000'))
