from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

static_path_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication_app.urls')),
    path('file/', include('filesystem.urls')),
] + static_path + static_path_media