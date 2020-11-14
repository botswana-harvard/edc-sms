from django.conf import settings
from edc_model_wrapper import ModelWrapper


class ContactModelWrapper(ModelWrapper):

    model = 'edc_sms.contact'
    next_url_attrs = ['subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'contact_listboard_url')
