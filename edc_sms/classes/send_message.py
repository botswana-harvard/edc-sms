import urllib

from django.apps import apps as django_apps

from ..models import Outgoing


class SendMessage:

    def __init__(
            self, message_data=None, mobile_number=None, mobile_numbers=None):
        self.message_data = message_data
        self.mobile_nuber = mobile_number
        self.mobile_numbers = mobile_numbers or []

    def sms_url(self, recipient_number=None, message_data=None):
        app_config = django_apps.get_app_config('edc_sms')
        base_api_url = app_config.base_api_url
        recepient_url_details = f'recipient={recipient_number}&'
        message_detais = f'messagetype=SMS:TEXT&messagedata={message_data}'
        url = base_api_url + recepient_url_details + message_detais
        return url

    def send(
            self, message_data=None, recipient_number=None,
            sms_type=None, schedule_datetime=None):
        recipient_number = recipient_number or self.mobile_nuber
        message_data = message_data or self.message_data
        url = self.sms_url(
            recipient_number=recipient_number, message_data=message_data)
        if schedule_datetime:
            str_schedule_datetime = schedule_datetime.strftime(
                "%y-%m-%d+%H:%M:%S")
            sms_schedule = f'&sendondate={str_schedule_datetime}'
            url += sms_schedule
        req = urllib.request.Request(url)
        urllib.request.urlopen(req)
        Outgoing.objects.create(
            mobile_number=recipient_number,
            text_data=message_data,
            action=sms_type)

    def send_multiple_contacts(self, message_data=None, mobile_numbers=[]):
        """Sends a message to multiple numbers.
        """
        mobile_numbers = mobile_numbers or self.mobile_numbers
        message_data = message_data or self.message_data
        for mobile_number in mobile_numbers:
            self.send(message_data=message_data, recipient_number=mobile_number)
