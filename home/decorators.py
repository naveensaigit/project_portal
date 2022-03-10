from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from home.models import Project
from functions import check_user_profile
from django.contrib import messages

def user_is_project_author(function):
    def wrap(request, *args, **kwargs):
        project_id = request.GET.get('project_id')
        project = Project.objects.get(pk=project_id)
        if project.FloatedBy == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_profile_completed(function):
    def wrap(request, *args, **kwargs):
        if check_user_profile(request.user):
            messages.error(request, 'Please complete your profile first.')
            return redirect(f'/profile/edit?firstLogin=True')
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap