# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def func1(request):
	return HttpResponse("1")

def func2(request):
	return HttpResponse("2")

def func3(request):
	return HttpResponse("3")

def func4(request):
	return HttpResponse("4")
