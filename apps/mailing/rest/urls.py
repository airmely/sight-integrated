from django.urls import path

from apps.mailing.rest.views import ExternalServiceView

app_name = "mailing"

urlpatterns = [
    path(
        "external-service/<int:msg_id>/",
        ExternalServiceView.as_view(),
        name="external-mail",
    ),
]
