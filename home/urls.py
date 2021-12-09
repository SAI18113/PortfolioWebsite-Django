from django.contrib import admin
from django.urls import path, include
from . import views
from home import models


# Django admin header customization
admin.site.site_header="Login to Developer Sai"
admin.site.site_title="Welcome to Sai's Dashboard"
admin.site.index_title="Welcome to this Portal"


urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    
]