from django.db import models

from apps.client.models import Tag, MobileOperatorCode


class Mailing(models.Model):
    start_datetime_mailing = models.DateTimeField(
        verbose_name="Начало запуска рассылки",
    )
    end_datetime_mailing = models.DateTimeField(
        verbose_name="Окончание рассылки",
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        verbose_name="Тема сообщения",
    )
    message = models.TextField(
        verbose_name="Сообщение",
    )
    mobile_operator_code = models.ManyToManyField(
        to=MobileOperatorCode,
        verbose_name="Мобильный код оператора",
    )
    tag = models.ManyToManyField(
        to=Tag,
        verbose_name="Тэг",
    )

    class Meta:
        _splash = "Рассылк%s"
        verbose_name = _splash % "а"
        verbose_name_plural = _splash % "и"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
