from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.profile, name = 'profile'),
    path('edit', views.profile_edit, name = 'profile-edit'),
    path('projects/applied', views.projects_applied, name = 'projects-applied'),
    path('projects/requested', views.projects_requested, name = 'projects-requested'),
    path('projects/starred', views.projects_starred, name = 'projects-starred'),
    path('projects/floated', views.projects_floated, name = 'projects-floated'),
]
