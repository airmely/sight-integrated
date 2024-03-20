# Generated by Django 5.0.3 on 2024-03-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0008_remove_mobileoperatorcode_mailing_remove_tag_mailing"),
        ("mailing", "0007_mailing_mobile_operator_code_mailing_tag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailing",
            name="mobile_operator_code",
        ),
        migrations.AddField(
            model_name="mailing",
            name="mobile_operator_code",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                to="client.mobileoperatorcode",
                verbose_name="Мобильный код оператора",
            ),
        ),
    ]