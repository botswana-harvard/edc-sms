from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import edc_sms_admin
from ..forms import ContactForm
from ..models import Contact
from .base_admin_model_mixin import ModelAdminMixin


@admin.register(Contact, site=edc_sms_admin)
class ContactAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContactForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'mobile_number',
                'alt_mobile_number',
                'first_name',
                'last_name')}),
        audit_fieldset_tuple
    )

    readonly_fields = ()

    list_display = [
        'created', 'subject_identifier', 'mobile_number',
        'user_created', 'user_modified', 'modified']

    list_filter = [
        'created', 'user_created', 'modified', 'user_modified']

    search_fields = (
        'subject_identifier', 'mobile_number', 'alt_mobile_number')
