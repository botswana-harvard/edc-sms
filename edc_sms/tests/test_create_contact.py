from django.test import TestCase

from ..models import Contact, Consent, Locator


class TestContat(TestCase):

    def setUp(self):
        self.consent = Consent.objects.create(
            subject_identifier='12345',
            first_name='test_firstname',
            last_name='test_surname')
        self.locator = Locator.objects.create(
            subject_identifier='12345',
            subject_cell='26771522602',
            subject_cell_alt='26771883071')

    def test_send_message(self):
        """Test creation of a outgoing message after sending sms.
        """
        contact = Contact.objects.all()
        self.assertEqual(contact.count(), 1)
