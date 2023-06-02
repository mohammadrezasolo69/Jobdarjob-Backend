from django.contrib import admin
from job.models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title','label','location','company_name','publication_date')