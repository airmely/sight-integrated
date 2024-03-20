from rest_framework import serializers
from phonenumber_field.validators import validate_international_phonenumber

from apps.client.models import Client, Tag, MobileOperatorCode


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("mobile_operator_code",)
        extra_kwargs = {
            "phone_number": {
                "validators": [validate_international_phonenumber],
                "required": True,
                "allow_null": False,
            }
        }


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class MobileOperatorCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileOperatorCode
        fields = "__all__"
