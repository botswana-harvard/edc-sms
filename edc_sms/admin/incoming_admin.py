from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import edc_sms_admin
from ..forms import IncomingForm
from ..models import Incoming
from .base_admin_model_mixin import ModelAdminMixin


@admin.register(Incoming, site=edc_sms_admin)
class IncomingAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = IncomingForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'mobile_number',
                'text_data',
                'action',)}),
        audit_fieldset_tuple
    )

    readonly_fields = ()

    list_display = [
        'created', 'subject_identifier', 'mobile_number',
        'user_created', 'user_modified', 'modified']

    list_filter = [
        'created', 'user_created', 'modified', 'user_modified']

    search_fields = ('subject_identifier', 'mobile_number')
