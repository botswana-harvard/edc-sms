from django.db import models

from .base_message import BaseMessage
from ..choices import OUTGOING_SMS_STATUS


class Outgoing(BaseMessage):

    is_delivered = models.BooleanField(default=False)

    is_sent = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=OUTGOING_SMS_STATUS)

    objects = models.Manager()

    class Meta:
        app_label = "edc_sms"
