from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    phone_number = PhoneNumberField(unique=True)
    operator_code = models.CharField(max_length=3, rel="client_filter_tag")
    tag = models.ForeignKey(
        to="Tag",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    timezone = ...


class Tag(models.Model):
    client_filter_tag = models.CharField(max_length=255)
