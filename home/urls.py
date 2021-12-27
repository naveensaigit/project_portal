from . import views
from django.urls import path


urlpatterns = [
    path('',views.main, name = 'home'),
    path('project/new', views.projectRegister, name='new-project'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('project/<int:project_id>/update',views.projectUpdate, name='update-project'),
    path('project/<int:project_id>/delete',views.projectDelete, name='delete-project'),
    path('project/<int:project_id>/apply/<int:page_number>/',views.projectApply, name='apply-to-project'),
    path('project/<int:project_id>/withdraw/<int:page_number>/',views.projectWithdraw, name='withdraw-from-project'),
    path('project/<int:project_id>/leave',views.projectLeave, name='leave-project'),
    path('project/<int:project_id>/star',views.projectStar, name='star-project'),
    path('project/<int:project_id>/unstar',views.projectUnStar, name='unstar-project'),
    path('project/<int:project_id>/accept/<request_user_name>',views.projectAccept, name='accept-project'),
    path('project/<int:project_id>/reject/<request_user_name>',views.projectReject, name='reject-project'),
]

