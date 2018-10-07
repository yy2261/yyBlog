# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from Article.models import Article

def article(request):
	art = Article.objects.get(id=1)
	response = '<h3>' + art.name + '</h3> </header>'
	for item in art.content.split('\n'):
		response += '<p>' + item + '</p>'
	context = {}
	context['content'] = response
	return render(request, 'articlePage.html', context)

def write(request):
	return render_to_response('write.html')
