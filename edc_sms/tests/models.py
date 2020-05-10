from django.db import models


class Locator(models.Model):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        null=True, blank=True,
        max_length=100)

    subject_cell = models.CharField(
        verbose_name='Cell number',
        max_length=100,
        blank=True,
        null=True)

    subject_cell_alt = models.CharField(
        verbose_name='Cell number (alternate)',
        max_length=100,
        blank=True,
        null=True)

    class Meta:
        app_label = "edc_sms"


class Consent(models.Model):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        null=True, blank=True,
        max_length=100)

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=100)

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=100)

    class Meta:
        app_label = "edc_sms"
