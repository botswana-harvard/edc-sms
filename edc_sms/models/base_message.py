from django.db import models

from django_crypto_fields.fields import EncryptedCharField, EncryptedTextField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import CellNumber
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugModelMixin as Base


from ..choices import SMS_TYPE


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('subject_identifier')
        fields.append('mobile_number')
        return fields

    class Meta:
        abstract = True


class BaseMessage(
        NonUniqueSubjectIdentifierFieldMixin,
        SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    mobile_number = EncryptedCharField(
        verbose_name='Mobile number',
        validators=[CellNumber, ],
        blank=True,
        null=True,
        help_text='')

    text_data = EncryptedTextField(max_length=255, blank=True)

    is_deleted = models.BooleanField(default=False)

    action = models.CharField(
        max_length=250,
        choices=SMS_TYPE,
        null=True,
        blank=True)

    class Meta:
        abstract = True
