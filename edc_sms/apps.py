from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_sms'
    verbose_name = 'Edc SMS'
    admin_site_name = 'edc_sms_admin'
    sms_api_username = ''
    sms_api_password = ''
    base_api_url = ''
