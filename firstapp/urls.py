from django.contrib import admin
from django.urls import path
from firstapp import views 
urlpatterns = [
    # path("", views.index, name='index')
    # path("about", views.about, name='about')
    path("contact", views.contact, name='contact')
    # path("services", views.services, name='service')
]
