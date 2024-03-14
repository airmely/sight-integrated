import logging

from celery import shared_task

from apps.mailing.services import (
    process_send_mailing_to_client,
    get_client_by_filter_of_tag_and_code_mobile_operator,
)

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def process_message_for_client():
    try:
        message = get_message_for_client()
        clients = get_client_by_filter_of_tag_and_code_mobile_operator()
        process_send_mailing_to_client(clients)

    except Exception as e:
        logger.exception(e)
