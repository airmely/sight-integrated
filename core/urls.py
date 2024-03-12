from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.client.rest.urls")),
    path("api/", include("apps.message.rest.urls")),
    path("api/", include("apps.mailing.rest.urls")),
]
