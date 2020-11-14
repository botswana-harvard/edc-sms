import urllib.request

from datetime import datetime
from django.apps import apps as django_apps
from django.utils.timezone import make_aware
from edc_base.utils import get_utcnow

import ssl

from ..models import Outgoing


class SendMessage:

    def __init__(
            self, message_data=None, mobile_number=None, mobile_numbers=None):
        self.message_data = message_data
        self.mobile_nuber = mobile_number
        self.mobile_numbers = mobile_numbers or []

    def sms_url(
            self, recipient_number=None, message_data=None, schedule_datetime=None):
        app_config = django_apps.get_app_config('edc_sms')
        base_api_url = app_config.base_api_url
        recepient_url_details = f'recipient={recipient_number}&'
        message_detais = f'messagetype=SMS:TEXT&messagedata={message_data}'
        url = base_api_url + recepient_url_details + message_detais
        print(url)
        return url

    def send(self, message_data=None, recipient_number=None,
             sms_type=None, schedule_datetime=None, subject_identifier=None):
        recipient_number = recipient_number or self.mobile_nuber
        message_data = message_data or self.message_data

        # Convert schedule_datetime to datetime object
        if isinstance(schedule_datetime, str):
            schedule_datetime = datetime.strptime(
                schedule_datetime, '%m/%d/%Y, %H:%M:%S')
            schedule_datetime = make_aware(schedule_datetime)

        url = self.sms_url(
            recipient_number=recipient_number,
            message_data=message_data,
            schedule_datetime=schedule_datetime)
        req = urllib.request.Request(url)
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            Outgoing.objects.create(
                mobile_number=recipient_number,
                text_data=message_data,
                schedule_datetime=schedule_datetime,
                action=sms_type)

            self.create_sms_model_obj(
                subject_identifier=subject_identifier,
                next_ap_date=schedule_datetime)

    def send_multiple_contacts(self, message_data=None, mobile_numbers=[]):
        """Sends a message to multiple numbers.
        """
        mobile_numbers = mobile_numbers or self.mobile_numbers
        message_data = message_data or self.message_data
        for mobile_number in mobile_numbers:
            self.send(
                message_data=message_data, recipient_number=mobile_number)

    def create_sms_model_obj(self, subject_identifier=None, next_ap_date=None):
        if subject_identifier:
            app_config = django_apps.get_app_config('edc_sms')
            sms_model_obj = django_apps.get_model(app_config.sms_model)
            sms_model_obj.objects.create(
                subject_identifier=subject_identifier,
                date_time_form_filled=get_utcnow(),
                next_ap_date=next_ap_date,
                date_reminder_sent=get_utcnow(),
                sms_outcome='sms_sent')
