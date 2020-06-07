import sys

from django.conf import settings

from .base_message import BaseMessage
from .contact import Contact
from .incoming import Incoming
from .outgoing import Outgoing
from .subject_consent_recipent_model_mixin import SubjectConsentRecipient

if 'edc_sms' in settings.APP_NAME and 'makemigrations' not in sys.argv:
    from ..tests.models import *
