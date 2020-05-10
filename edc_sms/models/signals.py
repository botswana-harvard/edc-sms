from django.apps import apps as django_apps
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Contact


@receiver(post_save, weak=False,
          dispatch_uid='create_contact_on_post_save')
def create_contact_on_post_save(
        sender, instance, raw, created, **kwargs):
    """Creates a protocol response.
    """
    app_config = django_apps.get_app_config('edc_sms')
    locator_mdl_cls = django_apps.get_model(
        app_config.locator_model)
    locator_auto_create_contact = app_config.locator_auto_create_contact
    locator_contact_map_fields = app_config.locator_contact_map_fields
    contact_options = {}
    if not raw:
        if locator_auto_create_contact:
            consent_mdl_cls = django_apps.get_model(
                app_config.consent_model)
            if instance.__class__ == locator_mdl_cls:
                consent_obj = consent_mdl_cls.objects.filter(
                    subject_identifier=instance.subject_identifier).last()
                contact_options.update(
                    subject_identifier=instance.subject_identifier,
                    first_name=consent_obj.first_name,
                    last_name=consent_obj.last_name,
                    mobile_number=getattr(
                        instance, locator_contact_map_fields.get(
                            'mobile_number')),
                    alt_mobile_number=getattr(
                        instance, locator_contact_map_fields.get(
                            'alt_mobile_number')))
                if contact_options.get('mobile_number'):
                    try:
                        Contact.objects.get(
                            mobile_number=contact_options.get('mobile_number'))
                    except Contact.DoesNotExist:
                        Contact.objects.create(
                            **contact_options)
