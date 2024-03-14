import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.mailing.rest.serializers import MailingMessageToClientsSerializer


class ExternalServiceView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=MailingMessageToClientsSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def post(self, request, msg_id) -> Response:
        serializer = MailingMessageToClientsSerializer(data=request.data)
        if serializer.is_valid():
            headers = {"Authorization": f"Bearer {settings.API_TOKEN}"}
            response = requests.post(
                f"{settings.URL_EXTERNAL_SERVICE}{msg_id}",
                json=serializer.validated_data,
                headers=headers,
            )
            return Response(response.json(), status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
