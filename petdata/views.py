# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import models

import json
# Create your views here.

def signUp(request):
	username = request.GET['username']
	password = request.GET['password']
	Attr = models.User(user_name = username , password = password)
	Attr.save()
	Attrjson = {'username': Attr.user_name}
	return HttpResponse(json.dumps(Attrjson))


def login(request):
	print request
	username = request.GET['username']
	password = request.GET['password']
	Attr = models.User.objects.get(user_name = username , password = password)
	Attrjson = {'username': Attr.user_name}
	return HttpResponse(json.dumps(Attrjson))
		

def createPet(request):
	owner = request.GET['username']
	petname = request.GET['petname']
	pet = models.Pet(pet_name = petname, owner = owner )
	pet.save()
	petstatus = model.Pet_State(pet_name = pet)
	return HttpResponse("success")

def petStatus(request):
	petname = request.GET['']
	return HttpResponse("3")

def func4(request):
	return HttpResponse("4")
