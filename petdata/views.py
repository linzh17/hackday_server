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
	AttrIf = models.User.objects.filter(user_name = username)
	if AttrIf==True :
		return HttpResponse("0")
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

def getPetStatus(request):
	petname = request.GET['petname']
	pet = models.Pet.objects.get(pet_name = petname)
	petstatus = pet.Pet_State
	status = {
		pet_hunger: petstatus.pet_hunger,
		pet_clean: petstatus.pet_hunger,
		pet_love: petstatus.pet_love
	}
	return HttpResponse(json.dumps(status))

def func4(request):
	return HttpResponse("4")
