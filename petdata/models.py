# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField("user_name",max_length=128,primary_key=True,default = "0")
    email = models.CharField("email",max_length=128,unique = True,default = "0")
    password = models.IntegerField(default=1) 

    friends = models.ForeignKey('self',null=True)
    pet = models.ForeignKey('Pet',null=True)

    def __str__(self):
        return 'User %s %s' %(self.user_name,self.email)

        
class Pet(models.Model):
    pet_name = models.CharField(max_length=128,primary_key=True,unique=True)
    #owner = models.ForeignKey(User)
    def __str__(self):
        return 'Pet %s' %(self.pet_name)


class Pet_State(models.Model):
    Pet_name= models.OneToOneField(Pet,primary_key=True, on_delete=models.CASCADE)
    pet_hunger = models.IntegerField(default=100)
    pet_clean = models.IntegerField(default=100)
    pet_love = models.IntegerField(default=0)

    def __str__(self):
        return 'Pet_State %s %s %s' %(self.pet_hunger,self.pet_clean,self.pet_love)