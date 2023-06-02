import django_filters

from job.models import Job


class JobFilter(django_filters.FilterSet):
    skills = django_filters.BaseCSVFilter(field_name='skills', lookup_expr='contains')

    class Meta:
        model = Job
        fields = (
            'label', 'company_name', 'category', 'location',
            'type_cooperation', 'skills'
        )
