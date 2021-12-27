import django_filters
from home.models import Project

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = [
            'Status',
            'Difficulty',
            'Duration',
            'FloatedBy'
        ]