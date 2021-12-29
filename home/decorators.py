from django.core.exceptions import PermissionDenied
from home.models import Project

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
