from django.test import TestCase

from apps.client.models import Client, Tag
from apps.client.tests.factories import ClientFactory, TagFactory


class ClientTestCase(TestCase):

    def setUp(self) -> None:
        self.client = ClientFactory()


class TagTestCase(TestCase):

    def setUp(self) -> None:
        self.tag = TagFactory()
