import sys

from django.conf import settings

from .base_message import BaseMessage
from .contact import Contact
from .incoming import Incoming
from .outgoing import Outgoing
from .subject_recipent_model_mixin import SubjectRecipientModelMixin

if 'edc_sms' in settings.APP_NAME:
    from ..tests.models import *
