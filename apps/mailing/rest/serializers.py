from rest_framework import serializers
from phonenumber_field.validators import validate_international_phonenumber

from apps.mailing.models import Mailing


class MailingMessageToClientsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    phone = serializers.CharField(validators=[validate_international_phonenumber])
    text = serializers.CharField()


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"
