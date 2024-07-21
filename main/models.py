from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Contact(models.Model):
	name = models.TextField(default="", null=True)
	email = models.CharField(default="",max_length=2000)
	phone = models.CharField(default="",max_length=1000)
	subject =	models.CharField(default="",max_length=1000)
	message = models.TextField(default="",max_length=1130, null=True)	
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name

class Apply(models.Model):
	name = models.TextField(default="Anonymous")
	cv = models.FileField(upload_to='account_files/profile_photos/', default="default_files/default_face.jpg")
	email = models.CharField(default="",max_length=2000)
	phone = models.CharField(default="",max_length=1000)
	address = models.CharField(default="",max_length=2000)
	start_date = models.CharField(default="",max_length=2000)
	position = models.CharField(default="",max_length=2000)
	qualification = models.TextField(default="",max_length=11130, null=True)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
