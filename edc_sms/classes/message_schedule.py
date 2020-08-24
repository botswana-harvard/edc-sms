from django_q.tasks import schedule


class MessageSchedule:

    def schedule_message(
            self, message_data=None, recipient_number=None,
            sms_type=None, schedule_datetime=None):
        # Schedule an sms
        schedule(
            'edc_sms.tasks.send_message',
            message_data,
            recipient_number,
            schedule_type='O',
            next_run=schedule_datetime)
