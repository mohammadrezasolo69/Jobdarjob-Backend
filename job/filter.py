import django_filters

from job.models import Job


class JobFilter(django_filters.FilterSet):
    TYPE_CHOICES = (
        ('تمام وقت','تمام وقت'),
        ('پاره وقت','پاره وقت')
    )
    skills = django_filters.BaseCSVFilter(field_name='skills', lookup_expr='contains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='contains')
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='contains')
    type_cooperation = django_filters.ChoiceFilter(field_name='type_cooperation',
                                                   choices=TYPE_CHOICES)

    class Meta:
        model = Job
        fields = (
            'label', 'company_name', 'category', 'location',
            'type_cooperation', 'skills'
        )