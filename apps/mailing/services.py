from typing import List, Optional

import requests
from django.conf import settings

from apps.client.models import Tag, MobileOperatorCode, Client
from apps.message.models import Message


def get_client_by_filter_of_tag_and_code_mobile_operator(
    timezone: Optional[str] = None,
    tags: Optional[List[Tag]] = None,
    mobile_operator: Optional[MobileOperatorCode] = None,
) -> Optional[List[Client]]:
    clients = Client.objects.prefetch_related("tag__client_set").filter(
        tags__in=tags,
        mobile_operator_code__in=mobile_operator,
        timezone=timezone,
    )
    return clients


def process_send_mailing_to_client(clients: List[Client], message: Message) -> None:
    for client in clients:
        headers = {"Authorization": f"Bearer {settings.API_TOKEN}"}
        response = requests.post(
            f"{settings.URL_EXTERNAL_SERVICE}{message.id}",
            json=client,
            headers=headers,
        )
