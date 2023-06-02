from rest_framework import routers

from job.api import viewset

router = routers.DefaultRouter()
router.register('', viewset.JobViewSet, basename='job')
urlpatterns = router.urls
