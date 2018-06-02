# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import models

import json
# Create your views here.

#登录验证部分
def signUp(request):
	print request
	username = request.POST['username']
	print username
	password = request.POST['password']
	email = request.POST['email']
	AttrIf = models.User.objects.filter(user_name = username)
	print "attif:",AttrIf
	if  (AttrIf) :
		print("chongFu")
		return HttpResponse("0")
	else:
		Attr = models.User(user_name = username , password = password, email = email)
		Attr.save()
		Attrjson = {'username': Attr.user_name}
		print Attrjson
		return HttpResponse(json.dumps(Attrjson))

def login(request):
	print request
	username = request.GET['username']
	password = request.GET['password']
	Attr = models.User.objects.filter(user_name = username , password = password)
	
	if (Attr):
		Attrjson = {'username': Attr.user_name}
		print("success login")
		return HttpResponse(json.dumps(Attrjson))
	else :
		print("error login")
		return HttpResponse("0")
	
#宠物有关部分　
def createPet(request):
	username = request.GET['username']
	petname = request.GET['petname']
	pet = models.Pet(pet_name = petname)
	pet.save()
	petstatus = models.Pet_State(pet_name = pet)
	user = models.User.objects.get(user_name = username)
	user.pet = pet
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

def showPet(request):
	pets = models.Pet.objects.all()
	peoples={}
	p_owners={}
	for pet in pets:
		owners = User.objects.filter(pet = pet).all()
		for owner in p_owners:
			p_owner = {"name":owner.user_name}
			p_owners.append(p_owner)
		people={"pet_name":pet.pet_name,"p_owners":p_owners}
		peoples.append(people)
	return HttpResponse(json.dumps(peoples))		
			

def func4(request):
	return HttpResponse("4")

#用户交际部分
def followFriends(request):
	username = request.GET['username']
	friendname = request.GET['friendname']
	user = models.User.objects.get(user_name = username)
	friend_user = models.User.objects.get(user_name = friendname)
	user.friends=friend_user
	friend_user.friends = user
	user.save()
	friend_user.save()
	return HttpResponse("success")

def havePet(request):
	 