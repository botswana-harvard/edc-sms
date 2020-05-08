from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_sms'
    verbose_name = 'Edc SMS'
