# -*- coding: utf-8 -*-

from django.http import HttpResponse

def blogTitle(request):
	return HttpResponse("yy的博客")
