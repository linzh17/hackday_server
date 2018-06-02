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
	if  (AttrIf) : #如果AttrIf不为空
		print("chongFu")
		return HttpResponse("0")
	else: #否则
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
	
	if (Attr): #如果Attr不为空
		Attrjson = {'username': Attr.user_name}
		print("success login")
		return HttpResponse(json.dumps(Attrjson))
	else : #否则
		print("error login")
		return HttpResponse("0")
	
def getUserStatus(request): #获取用户的宠物信息
	username = request.GET['username']
	user = models.User.objects.filter(user_name = username)
	pet = user.pet 
	if (pet):
		petjson = {
			petname : pet.pet_name,
		}
		HttpResponse(json.dumps(petjson))
	else HttpResponse("noPet")


#宠物有关部分　
def createPet(request):
	username = request.POST['username']
	petname = request.POST['petname']
	pet = models.Pet(pet_name = petname)
	pet.save()
	petstatus = models.Pet_State(pet_name = pet)
	user = models.User.objects.filter(user_name = username)
	user.pet = pet
	return HttpResponse("success")

def getPetStatus(request):
	petname = request.GET['petname']
	pet = models.Pet.objects.filter(pet_name = petname)
	petstatus = pet.Pet_State
	status = {
		pet_hunger: petstatus.pet_hunger,
		pet_clean: petstatus.pet_hunger,
		pet_love: petstatus.pet_love
	}
	return HttpResponse(json.dumps(status)) #返回宠物状态(json)

def showAllPet(request): #获得所有宠物及其主人们的信息
	pets = models.Pet.objects.all()
	peoples={}  #先声明以便append
	p_owners={} #先声明以便append
	for pet in pets: #循环
		owners = models.User.objects.filter(pet = pet).all() 
		for owner in owners:
			p_owner = {
				"name":owner.user_name， #必须加逗号
			}
			p_owners.append(p_owner)

		people={
			"pet_name":pet.pet_name,
			"p_owners":p_owners,
		}
		peoples.append(people)
	return HttpResponse(json.dumps(peoples))		

def showOnePet(request): #获得所有宠物及其主人们的信息
	p_owners={} #先声明以便append
	owners = models.User.objects.filter(pet = pet).all() 
	for owner in owners:
		p_owner = {
			"name":owner.user_name,
		}
		p_owners.append(p_owner)

	people={
		"pet_name":pet.pet_name,
		"p_owners":p_owners
	}
	
	return HttpResponse(json.dumps(people))


#用户交际部分
def followFriends(request):		#可能不需要
	username = request.POST['username']
	friendname = request.POST['friendname']
	user = models.User.objects.filter(user_name = username)
	friend_user = models.User.objects.filter(user_name = friendname)
	if not friend_user:
		return HttpResponse("Cannot find friend")
	user.friends=friend_user #把用户朋友值设为朋友 
	friend_user.friends = user #把朋友朋友值设为用户
	user.save()
	friend_user.save()
	return HttpResponse("success")

def havePet(request):	#领养已经有人在养的宠物
	username = request.POST['username']
	petname = request.POST['petname'] 
	user = User.objects.filter(user_name = username)
	pet = Pet.objects.filter(pet_name = petname)
	user.pet = pet
	user.save()
	return HttpResponse("success")

def feedPet(request):	#喂养宠物
	username = request.POST['username']
	petname = request.POST['petname']
	user = User.objects.filter(user_name = username)
	pet = Pet.objects.filter(pet_name = petname)
	pet.pet_state.pet_hunger = 	pet.pet_state.pet_hunger +10 #清洁度增加
	pet.pet_state.pet_love = pet.pet_state.pet_love + 1 #爱心增加
	pet.save()
	status = {
		petlove:pet.pet_state.pet_love,
		pethunger:pet.pet_state.pet_hunger
	}
	return HttpResponse(json.dumps(status)) #返回状态(json)

def cleanPet(request):	#清洗宠物
	username = request.POST['username']
	petname = request.POST['petname']
	user = User.objects.filter(user_name = username)
	pet = Pet.objects.filter(pet_name = petname)
	pet.pet_state.pet_clean = 	pet.pet_state.pet_clean +10 #清洁度增加
	pet.pet_state.pet_love = pet.pet_state.pet_love + 1 #爱心增加
	pet.save()
	status = {
		petlove:pet.pet_state.pet_love,
		pethunger:pet.pet_state.pet_clean
	}
	return HttpResponse(json.dumps(status)) #返回状态(json)


def func4(request):
	return HttpResponse("4")
