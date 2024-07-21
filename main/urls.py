from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path("", views.IndexView, name="index"),
	path("about/", views.AboutView, name="about"),
	path("faq/", views.FaqView, name="faq"),
	path("services/", views.ServicesView, name="services"),
	path("contact/", views.ContactView, name="contact"),
	path("apply/", views.ApplyView, name="apply"),
]