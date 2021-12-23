from . import views
from django.urls import path


urlpatterns = [
    path('',views.main, name = 'home'),
    path('project/new', views.projectRegister, name='new-project'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('project/<int:project_id>/update',views.projectUpdate, name='update-project'),
    path('project/<int:project_id>/delete',views.projectDelete, name='delete-project'),
]

