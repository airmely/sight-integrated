from django.db import models


class Mailing(models.Model):
    start_datetime_mailing = models.DateTimeField(
        verbose_name="Начало запуска рассылки",
    )
    end_datetime_mailing = models.DateTimeField(
        verbose_name="Окончание рассылки",
    )
    message = models.TextField(
        verbose_name="Сообщение",
    )
