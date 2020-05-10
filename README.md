[![Build Status](https://travis-ci.org/github/botswana-harvard/edc-sms.svg?branch=develop)](https://travis-ci.org/github/botswana-harvard/edc-sms) [![Coverage Status](https://coveralls.io/github/botswana-harvard/edc-sms/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-sms?branch=develop)

# edc-sms

This module uses `apscheduler`.

APScheduler for Django.

This little wrapper around APScheduler enables storing persistent jobs in the database using Django's ORM rather than requiring SQLAlchemy or some other bloatware.


## Installation

pip install django-apscheduler
pip install edc-sms

## Usage

Add django_apscheduler and edc_sms.apps.AppConfig to INSTALLED_APPS in your Django project settings, You can also specify a different format for displaying runtime timestamps in the Django admin site using APSCHEDULER_DATETIME_FORMAT:

		INSTALLED_APPS = (
		  ...
		  'django_apscheduler',
		  'edc_sms.apps.AppConfig',
		)

APSCHEDULER_DATETIME_FORMAT =  "N j, Y, f:s a"  # Default

Run migrations:

