from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register("clients", views.ClientViewSet, basename="clients")

app_name = "client"

urlpatterns = [
    path("", include(router.urls)),
]
