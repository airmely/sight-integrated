import logging

import requests
from django.conf import settings
from celery import shared_task

from apps.client.models import Client
from apps.mailing.models import Mailing
from apps.message.models import Message
from apps.mailing.rest.serializers import MailingMessageToClientsSerializer
from apps.mailing.services import (
    get_current_time,
    get_client_by_filter_of_tag_and_code_mobile_operator,
)

logger = logging.getLogger(__name__)


# @shared_task
def process_message_for_client(mailing):
    try:
        clients = get_client_by_filter_of_tag_and_code_mobile_operator(
            mailing.tag.all(), mailing.mobile_operator_code.all()
        )
        for client in clients:
            process_send_mailing_to_client(
                client=client,
                mailing=mailing,
            )
            logger.info(f"Sending message to client {client}")

    except Exception as e:
        logger.exception(e)


def process_send_mailing_to_client(client: Client, mailing) -> None:
    serializer = MailingMessageToClientsSerializer(
        data={
            "id": client.id,
            "phone": f"{client.phone_number}",
            "text": f"{mailing.message}",
        }
    )
    headers = {"Authorization": f"Bearer {settings.API_TOKEN}"}
    if serializer.is_valid():
        response = requests.post(
            f"{settings.URL_EXTERNAL_SERVICE}{mailing.id}",
            json=serializer.validated_data,
            headers=headers,
        )
        mailing_instance = Mailing.objects.get(id=mailing.id)
        if response.status_code != 200:
            Message.objects.create(
                client=client, mailing=mailing_instance, status=Message.Status.FAILED
            )
        else:
            Message.objects.create(
                client=client, mailing=mailing_instance, status=Message.Status.DELIVERED
            )
