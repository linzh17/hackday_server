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
		Attrjson = {'username': Attr.first().user_name}
		print("success login")
		return HttpResponse(json.dumps(Attrjson))
	else : #否则
		print("error login")
		return HttpResponse("0")
	
def getUserStatus(request): #获取用户的宠物信息
	username = request.GET['username']
	user = models.User.objects.filter(user_name = username).first()
	
	if (user):
		pet = user.pet
		petjson = {
			"petname" : pet.pet_name,
		}
		return HttpResponse(json.dumps(petjson))
	else:
		print("noPet")
		return HttpResponse("0")


#宠物有关部分　
def createPet(request):
	username = request.POST['username']
	petname = request.POST['petname']
	pet = models.Pet(pet_name = petname)
	pet.save()
	petstatus = models.Pet_State(Pet_name = pet)
	petstatus.save()
	user = models.User.objects.filter(user_name = username).first()
	user.pet = pet
	user.save()
	return HttpResponse("1")

def getPetStatus(request):
	petname = request.GET['petname']
	pet = models.Pet.objects.filter(pet_name = petname).first()
	petstatus = pet.pet_state
	status = {
		"pet_hunger": petstatus.pet_hunger,
		"pet_clean": petstatus.pet_hunger,
		"pet_love": petstatus.pet_love
	}
	return HttpResponse(json.dumps(status)) #返回宠物状态(json)

def showAllPet(request): #获得所有宠物及其主人们的信息
	pets = models.Pet.objects.all()
	peoples={}  #先声明以便append
	p_owners={} #先声明以便append
	i = 0
	for pet in pets: #循环
		owners = models.User.objects.filter(pet = pet).all() 
		for owner in owners:
			p_owner = {
				"name":owner.user_name, #必须加逗号
			}
			p_owners.append(p_owner)

		people={
			"pet_name":pet.pet_name,
			"p_owners":p_owners,
		}
		peoples.append(people)
	return HttpResponse(json.dumps(peoples))		

def showOnePet(request): #获得所有宠物及其主人们的信息
	petname = request.GET['petname']
	p_owners={} #先声明以便append
	pet = models.Pet.objects.filter(pet_name = petname).first()
	owners = models.User.objects.filter(pet = pet).all() 
	i = 0
	for owner in owners:
		p_owner = {
			"name":owner.user_name,
		}
		p_owners[i] = p_owner
		i += 1

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
	user = models.User.objects.filter(user_name = username).first()
	pet = models.Pet.objects.filter(pet_name = petname).first()
	user.pet = pet
	user.save()
	return HttpResponse("1")

def feedPet(request):	#喂养宠物
	#username = request.POST['username'] #不一定要
	petname = request.POST["petname"]
	#user = User.objects.filter(user_name = username) #不一定要
	pet = models.Pet.objects.filter(pet_name = petname).first()
	pet.pet_state.pet_hunger = 	pet.pet_state.pet_hunger +5 #清洁度增加
	pet.pet_state.pet_love = pet.pet_state.pet_love + 1 #爱心增加
	if pet.pet_state.pet_hunger > 100 :
		pet.pet_state.pet_hunger = 100
	pet.pet_state.save()
	status = {
		"petlove":pet.pet_state.pet_love,
		"pethunger":pet.pet_state.pet_hunger
	}
	return HttpResponse(json.dumps(status)) #返回状态(json)

def cleanPet(request):	#清洗宠物
	#username = request.POST['username'] #不一定要
	petname = request.POST['petname']
	#user = User.objects.filter(user_name = username) #不一定要
	pet = models.Pet.objects.filter(pet_name = petname).first()
	pet.pet_state.pet_clean = 	pet.pet_state.pet_clean +5 #清洁度增加
	pet.pet_state.pet_love = pet.pet_state.pet_love + 1 #爱心增加
	if pet.pet_state.pet_clean > 100 :
		pet.pet_state.pet_clean = 100
	pet.pet_state.save()
	status = {
		"petlove":pet.pet_state.pet_love,
		"petclean":pet.pet_state.pet_clean
	}
	return HttpResponse(json.dumps(status)) #返回状态(json)


#返回好友列表
def showFriends(request):
	username =  request.POST['username']
	user = User.objects.filter(user_name=username).first()
	friends = User.objects.filter(friends= user).all()
	peoples={}
	for friend in friends:
		people={"username":friend.user_name,"pet":friend.pet,}
		peoples.append(people)

	return HttpResponse(json.dump(peoples))	 	




def func4(request):
	return HttpResponse("4")
