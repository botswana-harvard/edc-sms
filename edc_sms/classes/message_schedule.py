from .send_message import SendMessage
from django_q.tasks import schedule


class MessageSchedule:

    send_message = SendMessage

    def schedule_message(
            self, message_data=None, recipient_number=None,
            sms_type=None, schedule_datetime=None):
        # Schedule an sms
        schedule(
            'edc_sms.classes.SendMessage.send',
            message_data,
            recipient_number,
            sms_type,
            schedule_datetime,
            schedule_type='O',
            next_run=schedule_datetime)
