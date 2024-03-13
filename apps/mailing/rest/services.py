from typing import List

from apps.client.models import Tag, MobileOperatorCode, Client


def get_client_by_filter_of_tag_and_code_mobile_operator(
    tags: List[Tag],
    mobile_operator: MobileOperatorCode,
) -> Client:
    pass
