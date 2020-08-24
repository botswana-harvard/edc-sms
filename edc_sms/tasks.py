from Crypto import Random

from .classes import SendMessage


def send_message(message_data=None, recipient_number=None,
                 schedule_datetime=None):
    """Task to send scheduled message to participant."""

    Random.atfork()

    sms = SendMessage(message_data, recipient_number)
    sms.send(schedule_datetime)
