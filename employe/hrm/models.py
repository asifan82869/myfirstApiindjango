# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
	employee_id = models.CharField(max_length = 10, unique = True)
	name = models.CharField(max_length = 100)
	age = models.IntegerField()
	ranking = models.FloatField()

	def __str__(self):
		return self.employee_id+" - "+self.name