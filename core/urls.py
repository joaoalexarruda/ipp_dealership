from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Frontend URLs
    path('', include('pages.urls')),
    path('', include('motorcycles.urls')),
    path('', include('accounts.urls')),
    path('', include('cars.urls')),
    # Backend URLs

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
