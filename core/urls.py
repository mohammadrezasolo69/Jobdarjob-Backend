from django.contrib import admin
from django.urls import path, include

urlpatterns_api_v1 = []

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(urlpatterns_api_v1))
]

# ----------------------------------- Config Static ------------------------------------
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
