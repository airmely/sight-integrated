from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions

from .serializers import MessageSerializer
from ..models import Message


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        operation_description="This endpoint allows administrators to perform CRUD operations on messages.",
        responses={200: openapi.Response("Successful operation"), 400: "Bad request"},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
