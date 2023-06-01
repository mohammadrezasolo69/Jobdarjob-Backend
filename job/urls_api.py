from django.urls import path, include

app_name = 'job'
urlpatterns = [
    path('', include('job.api.router'))
]
