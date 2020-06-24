# Generated by Django 3.0.7 on 2020-06-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_identifier', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subject Identifier')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Locator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_identifier', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subject Identifier')),
                ('subject_cell', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cell number')),
                ('subject_cell_alt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cell number (alternate)')),
            ],
        ),
    ]
