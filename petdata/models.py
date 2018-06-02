# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    pass

class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    pet_name = models.CharField(max_length = 100)
    user_list = models.ForeignKey(User)

    def __str__(self):
        return '<Pet %s>' % (self.pet_name)

class Pet_State(models.Model):
    pet = models.OneToOneField(Pet,primary_key = True)
    pet_clean = models.IntegerField()
    pet_hunger = models.IntegerField()

    def __str__(self):
        return '<Pet_state %s %s %s>' %(self.pet,self.pet_clean,self.pet_hunger)

class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    user_info = models.ForeignKey(User)
    cookies = models.BooleanField() 
    soap = models.BooleanField()

    def __str__(self):
        return '<Goods %s %s %s>' %(self.name,self.cookies,self.soap)
