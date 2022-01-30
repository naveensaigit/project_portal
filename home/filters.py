import django_filters
from home.models import Project

class ProjectFilter(django_filters.FilterSet):
    FilteredBy = django_filters.ChoiceFilter()
    class Meta:
        model = Project
        fields = [
            'Status',
            'Difficulty',
            # 'Duration',
            'FloatedBy',
            'Tags',
            'FilteredBy'
        ]
    @property
    def qs(self):
        qs = super().qs
        if len(self.data):
            Tags = self.data.getlist('Tags')
            FilterBy = self.data.get('FilterBy')
            if FilterBy == 'And':
                for x in Tags:
                    qs = qs.filter(Tags__in = [x])
        return qs