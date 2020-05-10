from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import edc_sms_admin
from ..forms import OutgoingForm
from ..models import Outgoing
from .base_admin_model_mixin import ModelAdminMixin


@admin.register(Outgoing, site=edc_sms_admin)
class OutgoingAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = OutgoingForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'mobile_number',
                'text_data',
                'status',
                'action',)}),
        audit_fieldset_tuple
    )

    radio_fields = {
        "status": admin.VERTICAL}

    readonly_fields = ()

    list_display = [
        'created', 'subject_identifier', 'mobile_number',
        'status', 'user_created', 'user_modified', 'modified']

    list_filter = [
        'status', 'created', 'user_created', 'modified', 'user_modified']

    search_fields = ('subject_identifier', 'mobile_number')
