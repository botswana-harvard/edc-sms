from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'edc_sms'
    verbose_name = 'Edc SMS'
    admin_site_name = 'edc_sms_admin'
    identifier_pattern = None
    locator_auto_create_contact = True
    locator_model = 'edc_sms.locator'
    consent_model = 'edc_sms.consent'
    sms_model = 'edc_sms.sms'
    locator_contact_map_fields = {
        'mobile_number': 'subject_cell',
        'alt_mobile_number': 'subject_cell_alt'}
    base_api_url = settings.BASE_API_URL

    def ready(self):
        from .models.signals import create_contact_on_post_save
