from django.test import TestCase

from ..classes import SendMessage
from ..models import Contact, Outgoing


class TestDataActionItem(TestCase):

    def setUp(self):

        # Enter a valid mobile number for contact.
        self.contact = Contact.objects.create(
            subject_identifier='123124',
            first_name='TUser',
            last_name='TUser',
            mobile_number='')
        self.contact2 = Contact.objects.create(
            subject_identifier='123125',
            first_name='TUser2',
            last_name='TUser2',
            mobile_number='')
        self.contact2 = Contact.objects.create(
            subject_identifier='123125',
            first_name='TUser2',
            last_name='TUser2',
            mobile_number='')
        self.text_data = (
            f'Hello+{self.contact.first_name}+'
            f'{self.contact.last_name}.+Have+a+good+day.')
        self.text_data2 = ('Dear+Our+valued+participants+please+'
                           'wash+your+hands+and+stay+home.')

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
