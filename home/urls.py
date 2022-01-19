from . import views
from django.urls import path


urlpatterns = [
    path('',views.main, name = 'home'),
    path('tag/new/',views.createNewTag, name = 'new-tag'),
    path('project/new/', views.projectRegister, name='new-project'),
    path('project/', views.project, name='project'),
    path('project/update/',views.projectUpdate, name='update-project'),
    path('project/delete/',views.projectDelete, name='delete-project'),
    path('project/task/',views.projectTask, name='task-project'),
    path('project/accept/',views.projectAccept, name='accept-project'),
    path('project/reject/',views.projectReject, name='reject-project'),
]

