from django_q.tasks import schedule


class MessageSchedule:

    def schedule_message(
            self, message_data=None, recipient_number=None,
            sms_type=None, schedule_datetime=None, subject_identifier=None):

        # Convert schedule_datetime to string to parse to the schedule func
        schedule_datetime_str = schedule_datetime.strftime(
            '%m/%d/%Y, %H:%M:%S')

        # Schedule an sms
        schedule(
            'edc_sms.tasks.send_message',
            message_data,
            recipient_number,
            schedule_datetime_str,
            subject_identifier,
            schedule_type='O',
            next_run=schedule_datetime)
