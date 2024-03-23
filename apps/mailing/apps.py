from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.mailing"

    def ready(self):
        from .signals import run_celery_task_on_mailing_creation
