from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from utils import SightIntegratedAPISchemaGenerator


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
    path(
        "api/docs/",
        get_schema_view(
            info=openapi.Info(
                title="Sight-Integrated API",
                default_version="v1",
            ),
            generator_class=SightIntegratedAPISchemaGenerator,
        ).with_ui("swagger"),
    ),
    path(
        "api/redoc/",
        get_schema_view(
            info=openapi.Info(
                title="Sight-Integrated API",
                default_version="v1",
            ),
            generator_class=SightIntegratedAPISchemaGenerator,
        ).with_ui("redoc"),
    ),
]
