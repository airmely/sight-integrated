# Generated by Django 5.0.3 on 2024-03-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_remove_client_tag_client_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="tag",
            field=models.ManyToManyField(
                blank=True, to="client.tag", verbose_name="Тэг"
            ),
        ),
    ]