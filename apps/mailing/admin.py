from django.contrib import admin

from apps.mailing.models import Mailing
from apps.mailing.tasks import process_message_for_client


def action_mailing_send_by_client(model, request, queryset):
    process_message_for_client(queryset.first())


action_mailing_send_by_client.short_description = "Send mailing by client"


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    filter_horizontal = ("tag", "mobile_operator_code")
    actions = [action_mailing_send_by_client]
