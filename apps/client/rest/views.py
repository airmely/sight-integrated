from rest_framework import permissions
from rest_framework import viewsets

from apps.client.models import Client, Tag, MobileOperatorCode
from apps.client.rest.serializers import (
    ClientSerializer,
    TagSerializer,
    MobileOperatorCodeSerializer,
)


class ClientViewSet(viewsets.ModelViewSet):
    """CLIENTS API"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]


class TagViewSet(viewsets.ModelViewSet):
    """TAGS API"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]


class MobileOperatorCodeViewSet(viewsets.ModelViewSet):
    """MobileOperatorCode API"""

    queryset = MobileOperatorCode.objects.all()
    serializer_class = MobileOperatorCodeSerializer
    permissions_classes = [permissions.AllowAny]
