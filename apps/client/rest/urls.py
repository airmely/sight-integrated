from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(
    "clients",
    views.ClientViewSet,
    basename="clients",
)
router.register(
    "tags",
    views.TagViewSet,
    basename="tags",
)
router.register(
    "mobile_operator_code",
    views.MobileOperatorCodeViewSet,
    basename="mobile_operator",
)

app_name = "client"

urlpatterns = [
    path("", include(router.urls)),
]
