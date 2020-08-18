from datetime import timedelta

from django.test import TestCase

from ..classes import SendMessage
from ..models import Contact, Outgoing


class TestSendMessage(TestCase):

    def setUp(self):

        # Enter a valid mobile number for contact.
        self.contact = Contact.objects.create(
            subject_identifier='123124',
            first_name='TUser',
            last_name='TUser',
            mobile_number='26771522602')
        self.contact2 = Contact.objects.create(
            subject_identifier='123125',
            first_name='TUser2',
            last_name='TUser2',
            mobile_number='26771883071')
        self.contact2 = Contact.objects.create(
            subject_identifier='123125',
            first_name='TUser2',
            last_name='TUser2',
            mobile_number='26774720855')
        self.text_data = (
            f'Hello+{self.contact.first_name}+'
            f'{self.contact.last_name}.+Have+a+good+day.')
        self.text_data2 = ('Dear+Our+valued+participants+please+'
                           'wash+your+hands+and+stay+home.+Coulson+Kgathi+Testing')

    def test_send_message(self):
        """Test creation of a outgoing message after sending sms.
        """
        sms = SendMessage(
            mobile_number=self.contact.mobile_number,
            message_data=self.text_data)
        sms.send()
        outgoing_message = Outgoing.objects.all()
        self.assertEqual(outgoing_message.count(), 1)

    def test_send_messages(self):
        """Test creation of a outgoing messages after sending smses.
        """
        mobile_numbers = []
        contacts = Contact.objects.all()
        self.assertEqual(contacts.count(), 3)
        for contact in contacts:
            mobile_numbers.append(contact.mobile_number)
        sms = SendMessage(
            mobile_numbers=mobile_numbers,
            message_data=self.text_data2)
        sms.send_multiple_contacts()
        outgoing_message = Outgoing.objects.all()
        self.assertEqual(outgoing_message.count(), 3)

    def test_scheduled_messages(self):
        """Test sending a schedule message.
        """
        from pytz import timezone
        import datetime
        d = datetime.datetime.now()
        schedule = d + timedelta(minutes=2)
        schedule = schedule.astimezone(timezone('Africa/Gaborone'))
        sms = SendMessage(
            mobile_number=self.contact.mobile_number,
            message_data=self.text_data)
        sms.send(schedule_datetime=schedule)
        outgoing_message = Outgoing.objects.all()
        self.assertEqual(outgoing_message.count(), 1)
