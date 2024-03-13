from django.contrib import admin

from apps.message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
