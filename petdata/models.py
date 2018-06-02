# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField("user_name",max_length=128,primary_key=True,default = "0")
    email = models.CharField("email",max_length=128,unique = True,default = "0")
    password = models.IntegerField(default=1) 

    #friends = models.ForeignKey(User)

    def __str__(self):
        return 'User %s %s' %(self.user_name,self.email)

        
