from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Count

from django.core.mail import send_mail
from . models import *
from datetime import datetime
import datetime as dt


def IndexView(request):

	if request.method == "POST":
		pass

	else:
		
		context = {}
		return render(request, "main/index.html", context )


def AboutView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/about.html", context )


def FaqView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/faq.html", context )



def ContactView(request):

	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("name")
		subject = request.POST.get("subject")
		phone = request.POST.get("phone")
		message = request.POST.get("message")

		contact = Contact.objects.create(
			name=name,  
			email=email, 
			subject=subject, 
			phone=phone, 
			message=message, 
		)
		contact.save()

		messages.warning(request, "Message Delivered!")
		return HttpResponseRedirect(reverse("main:index"))

	else:

		context = {}
		return render(request, "main/contact.html", context )


def ApplyView(request):

	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("name")
		qualification = request.POST.get("qualification")
		phone = request.POST.get("phone")
		address = request.POST.get("address")
		position = request.POST.get("position")
		start_date = request.POST.get("start_date")
		cv = request.FILES.get("cv")

		application = Apply.objects.create(
			name=name,  
			email=email, 
			qualification=qualification, 
			phone=phone, 
			address=address,
			position=position,
			start_date=start_date,
			cv=cv 
		)
		application.save()

		messages.warning(request, "Application Submitted!")
		return HttpResponseRedirect(reverse("main:index"))

	else:

		context = {}
		return render(request, "main/apply.html", context )


def ServicesView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/services.html", context )