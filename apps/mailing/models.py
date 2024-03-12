from django.db import models
from django.db.models import Q


class Mailing(models.Model):
    start_datetime_mailing = models.DateTimeField()
    end_datetime_mailing = models.DateTimeField()
    message = models.TextField()
    client_properties_filter = models.FilteredRelation(
        "Tag", condition=Q(name="client_filter_tag")
    )
