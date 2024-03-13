from factory.django import DjangoModelFactory
from factory import Faker

from apps.client.models import Client, Tag


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    phone_number = Faker("phone_number")
    code = Faker("code")


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    client_filter_tag = Faker("client_filter_tag")
