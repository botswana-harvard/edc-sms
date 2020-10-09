from Crypto import Random

from .classes import SendMessage


def send_message(message_data=None, recipient_number=None,
                 schedule_datetime=None, subject_identifier=None):
    """Task to send scheduled message to participant."""

    Random.atfork()

    sms = SendMessage()
    sms.send(message_data=message_data, recipient_number=recipient_number,
             schedule_datetime=schedule_datetime, subject_identifier=subject_identifier)
