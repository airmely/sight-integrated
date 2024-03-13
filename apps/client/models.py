from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    phone_number = PhoneNumberField(
        unique=True,
        verbose_name="Номер телефона",
    )
    mobile_operator_code = models.ForeignKey(
        to="MobileOperatorCode",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="Мобильный код оператора",
    )
    tag = models.ForeignKey(
        to="Tag",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Тэг",
    )
    timezone = models.CharField(
        max_length=50,
        verbose_name="Часовой пояс",
    )


class Tag(models.Model):
    client_filter_tag = models.CharField(
        max_length=50,
    )


class MobileOperatorCode(models.Model):
    operator_code = models.PositiveSmallIntegerField()
