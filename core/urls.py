from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from utils import SightIntegratedAPISchemaGenerator
from apps.client.rest.urls import urlpatterns as client_urls
from apps.message.rest.urls import urlpatterns as message_urls
from apps.mailing.rest.urls import urlpatterns as mailing_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(client_urls)),
    path("api/", include(message_urls)),
    path("api/", include(mailing_urls)),
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
