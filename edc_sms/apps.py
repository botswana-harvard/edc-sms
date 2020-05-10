from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'edc_sms'
    verbose_name = 'Edc SMS'
    admin_site_name = 'edc_sms_admin'
    base_api_url = settings.BASE_API_URL
