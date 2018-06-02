# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.

import models
 
 
admin.site.register(models.User)
admin.site.register(models.Pet)
admin.site.register(models.Pet_State)
