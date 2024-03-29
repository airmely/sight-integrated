# Generated by Django 5.0.3 on 2024-03-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={"verbose_name": "Сообщение", "verbose_name_plural": "Сообщения"},
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
            ),
        ),
    ]
