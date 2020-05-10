from django.db import models

from django_crypto_fields.fields import EncryptedCharField
from django_crypto_fields.fields import FirstnameField, LastnameField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import CellNumber
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base

from edc_constants.choices import GENDER_UNDETERMINED


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('mobile_number')
        fields.append('subject_identifier')
        return fields

    class Meta:
        abstract = True


class ContactManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, mobile_number):
        return self.get(mobile_number=mobile_number)


class Contact(
        NonUniqueSubjectIdentifierFieldMixin,
        SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    first_name = FirstnameField(
        null=True, blank=True)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=True)

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=True)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_UNDETERMINED,
        max_length=1,
        null=True,
        blank=True)

    mobile_number = EncryptedCharField(
        verbose_name='Mobile number',
        validators=[CellNumber, ],
        blank=False,
        null=True,
        help_text='')

    alt_mobile_number = EncryptedCharField(
        verbose_name='Alternative Mobile number',
        validators=[CellNumber, ],
        blank=True,
        null=True,
        help_text='')

    class Meta:
        app_label = "edc_sms"
