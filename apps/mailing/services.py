from typing import List
from pytz import timezone
from datetime import datetime, timedelta

from django.db.models import Q

from apps.client.models import Tag, MobileOperatorCode, Client


def get_client_by_filter_of_tag_and_code_mobile_operator(
    tags: List[Tag],
    mobile_operator: List[MobileOperatorCode],
) -> List[Client]:
    clients = (
        Client.objects.filter(
            Q(tag__in=tags) | Q(mobile_operator_code__in=mobile_operator)
        )
        .distinct()
        .only("phone_number")
    )
    return clients


def get_current_time(client_timezone: str) -> datetime:
    now = datetime.now()
    tz = timezone(client_timezone)
    eta_time = tz.localize(now + timedelta(hours=1))
    return eta_time
