# Generated by Django 5.0.3 on 2024-03-13 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0003_alter_client_tag"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "Клиент%s", "verbose_name_plural": "Клиенты"},
        ),
        migrations.AlterField(
            model_name="client",
            name="client_timezone",
            field=models.ForeignKey(
                default=None,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_set",
                to="client.timezone",
                verbose_name="Часовой пояс",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="tag",
            field=models.ManyToManyField(
                blank=True,
                related_name="%(class)s_set",
                to="client.tag",
                verbose_name="Тэг",
            ),
        ),
    ]
