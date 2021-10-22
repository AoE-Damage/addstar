from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search"),
    path("contact", views.contact, name="contact"),
    path("contact-blogger/<str:pk>", views.contact_blogger, name="contact_blogger"),
    path("success", views.success, name="success"),
]
