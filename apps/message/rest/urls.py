from django.urls import path, include
from rest_framework import routers
from apps.message.rest.views import MessageViewSet

router = routers.SimpleRouter()

router.register("messages", MessageViewSet, basename="messages")

app_name = "message"

urlpatterns = [
    path("", include(router.urls)),
]
