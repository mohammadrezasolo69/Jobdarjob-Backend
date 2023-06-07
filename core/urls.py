from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views as drf_spectacular_view

urlpatterns_api_v1 = [
    path('jobs/', include('job.urls_api'),name='job_api')
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # urls drf_spectacular
    path('', drf_spectacular_view.SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/schema/', drf_spectacular_view.SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/v1/schema/swagger-ui/', drf_spectacular_view.SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    # urls my apps
    path('api/v1/', include(urlpatterns_api_v1))
]

# ----------------------------------- Config Static ------------------------------------
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Config django-silk
    urlpatterns += [path('monitoring/silk/', include('silk.urls', namespace='silk'))]
