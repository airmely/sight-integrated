from rest_framework import permissions
from rest_framework import viewsets

from apps.client.models import Client
from apps.client.rest.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
