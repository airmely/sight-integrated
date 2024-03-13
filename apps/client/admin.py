from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Client

admin.site.unregister(Group)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ["mobile_operator_code"]
    filter_horizontal = ("tag",)
