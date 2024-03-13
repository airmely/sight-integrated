from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


_RELATED_NAME_SET = "%(class)s_set"


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
    tag = models.ManyToManyField(
        to="Tag",
        blank=True,
        verbose_name="Тэг",
        related_name=_RELATED_NAME_SET,
    )
    client_timezone = models.ForeignKey(
        to="TimeZone",
        on_delete=models.CASCADE,
        verbose_name="Часовой пояс",
        max_length=50,
        null=True,
        default=None,
        related_name=_RELATED_NAME_SET,
    )

    class Meta:
        _splash = "Клиент%s"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"

    def __str__(self):
        return f"{self.phone_number} - {self.client_timezone}"

    def save(self, *args, **kwargs):
        operator_code = "".join(filter(str.isdigit, str(self.phone_number)))
        operator_code = int(str(operator_code)[1:4])
        mobile_operator = MobileOperatorCode.objects.get(operator_code=operator_code)
        self.mobile_operator_code = mobile_operator
        super().save(*args, **kwargs)


class Tag(models.Model):
    client_filter_tag = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.client_filter_tag


class MobileOperatorCode(models.Model):
    operator_code = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["operator_code"]

    def __str__(self):
        return f"{self.operator_code}"


class TimeZone(models.Model):
    timezone = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.timezone
