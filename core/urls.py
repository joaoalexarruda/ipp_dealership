from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("", include("motorcycles.urls")),
    path("", include("accounts.urls")),
    path("", include("cars.urls")),
    path("api/v1/", include("api.urls")),
    path("api/v1/auth/", include("authentication.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
