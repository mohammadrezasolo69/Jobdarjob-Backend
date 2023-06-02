from rest_framework import serializers

from job.models import Job


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id', 'link', 'label', 'company_name', 'company_cover', 'company_website',
            'company_category', 'title', 'category', 'location', 'type_cooperation', 'work_experience',
            'salary', 'description', 'company_about', 'gender', 'education', 'military_service', 'skills',
            'date_last_crawl', 'publication_date'
        )
