# Generated by Django 5.0.3 on 2024-03-19 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0008_remove_mobileoperatorcode_mailing_remove_tag_mailing"),
        ("mailing", "0008_remove_mailing_mobile_operator_code_and_more"),
        ("message", "0002_alter_message_options_alter_message_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="client",
        ),
        migrations.AlterField(
            model_name="message",
            name="mailing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mailing_messages",
                to="mailing.mailing",
                verbose_name="Рассылка",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="status",
            field=models.CharField(
                choices=[
                    ("QUEUED", "В очереди"),
                    ("FAILED", "Не успешно"),
                    ("DELIVERED", "Доставлено"),
                ],
                default="QUEUED",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="client",
            field=models.ManyToManyField(to="client.client", verbose_name="Клиенты"),
        ),
    ]
