from .send_message import SendMessage


class MessageSchedule:

    send_message = SendMessage

    def schedule_message(
            self, message_data=None, recipient_number=None,
            sms_type=None, schedule_datetime=None):
        # Schedule an sms
        self.send_message().send(
            message_data=message_data,
            recipient_number=recipient_number,
            sms_type=sms_type,
            schedule_datetime=schedule_datetime)
