from django.db import models

from .base_message import BaseMessage


class Incoming(BaseMessage):

    is_rejected = models.BooleanField(default=False)

    is_error = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.subject_identifier}'

    def natural_key(self):
        return self.subject_identifier

    class Meta:
        app_label = "edc_sms"
