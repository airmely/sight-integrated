from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("client/", include("apps.client.rest.urls")),
                path("message/", include("apps.message.rest.urls")),
                path("mailing/", include("apps.mailing.rest.urls")),
            ]
        ),
    ),
]
