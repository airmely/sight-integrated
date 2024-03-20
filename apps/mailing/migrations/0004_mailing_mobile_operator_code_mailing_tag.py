# Generated by Django 5.0.3 on 2024-03-19 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0006_alter_client_phone_number"),
        ("mailing", "0003_alter_mailing_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="mobile_operator_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="client.mobileoperatorcode",
                verbose_name="Мобильный код оператора",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="tag",
            field=models.ManyToManyField(
                blank=True, null=True, to="client.tag", verbose_name="Тэг"
            ),
        ),
    ]