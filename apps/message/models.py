from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    class Status(models.TextChoices):
        QUEUED = "QUEUED", _("QUEUED")
        DELIVERY = "DELIVERY", _("DELIVERY")
        FAILED = "FAILED", _("FAILED")

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.QUEUED,
    )
    mailing = models.ForeignKey(
        to="Mailing",
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        to="Client",
        on_delete=models.CASCADE,
    )
