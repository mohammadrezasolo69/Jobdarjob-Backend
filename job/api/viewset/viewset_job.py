from django_filters import rest_framework as filters
from rest_framework import viewsets

from job.api.serializer import JobListSerializer, JobDetailSerializer
from job.filter import JobFilter
from job.models import Job


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    model = Job
    lookup_field = 'id'
    serializer_class = JobDetailSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobFilter

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return JobListSerializer
        return self.serializer_class
