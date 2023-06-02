from rest_framework import serializers

from job.models import Job


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id', 'link', 'label', 'company_name', 'company_cover',
            'title', 'category', 'location', 'type_cooperation',
            'publication_date', 'salary', 'skills','work_experience'
        )
