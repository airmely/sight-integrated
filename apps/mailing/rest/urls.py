from django.urls import path, include
from rest_framework import routers

from apps.mailing.rest import views

router = routers.SimpleRouter()

router.register("mailing", views.MailingViewSet, basename="mailing-list")

app_name = "mailing"

urlpatterns = [
    path("", include(router.urls)),
    path(
        "external-service/<int:msg_id>/",
        views.ExternalServiceView.as_view(),
        name="external-mail",
    ),
]
