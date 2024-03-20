import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.mailing.models import Mailing
from apps.mailing.services import get_current_time
from apps.mailing.tasks import process_message_for_client

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Mailing)
def run_celery_task_on_mailing_creation(sender, instance, created, **kwargs):
    logger.info(f"Mailing {instance.id} created")
    if created:
        eta = get_current_time(instance.client_timezone.timezone)
        process_message_for_client.delay(instance)
