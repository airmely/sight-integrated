from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.mailing.models import Mailing
from apps.client.models import Client


class Message(models.Model):
    class Status(models.TextChoices):
        QUEUED = "QUEUED", _("В очереди")
        FAILED = "FAILED", _("Не успешно")
        DELIVERED = "DELIVERED", _("Доставлено")

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.QUEUED,
    )
    mailing = models.ForeignKey(
        to=Mailing,
        on_delete=models.CASCADE,
        related_name="mailing_messages",
    )
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
    )

    class Meta:
        _splash = "Сообщени%s"
        verbose_name = _splash % "е"
        verbose_name_plural = _splash % "я"

    def __str__(self):
        return f"{self.client} - {self.mailing} - {self.status}"
