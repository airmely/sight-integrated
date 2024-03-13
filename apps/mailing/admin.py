from django.contrib import admin

from apps.mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    pass
