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


class SMS(models.Model):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=100,
        null=True, blank=True,)

    date_time_form_filled = models.DateTimeField(
        verbose_name='Date SMS form filled',
        null=True, blank=True)

    next_ap_date = models.DateField(
        verbose_name='Date of next appointment (referral or return)',
        null=True, blank=True,)

    date_reminder_sent = models.DateField(
        verbose_name='Date visit reminder SMS sent',
        null=True, blank=True,)

    sms_outcome = models.CharField(
        verbose_name='Outcome of reminder SMS',
        max_length=50,
        null=True, blank=True)

    class Meta:
        app_label = 'edc_sms'
