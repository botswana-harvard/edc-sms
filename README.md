[![Build Status](https://travis-ci.org/github/botswana-harvard/edc-sms.svg?branch=develop)](https://travis-ci.org/github/botswana-harvard/edc-sms) [![Coverage Status](https://coveralls.io/github/botswana-harvard/edc-sms/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-sms?branch=develop)

# edc-sms

This module uses `apscheduler`.

APScheduler for Django.

This little wrapper around APScheduler enables storing persistent jobs in the database using Django's ORM rather than requiring SQLAlchemy or some other bloatware.


## `Installation`

pip install django-apscheduler

pip install edc-sms

### `Usage`

Add django_apscheduler and edc_sms.apps.AppConfig to INSTALLED_APPS in your Django project settings, You can also specify a different format for displaying runtime timestamps in the Django admin site using APSCHEDULER_DATETIME_FORMAT:

	`settings.py`
	
		....
		import os
		import sys
		import configparser
		
		APP_NAME = 'your_app_name'
		
		CONFIG_FILE = f'{APP_NAME}.ini'
		CONFIG_PATH = os.path.join(ETC_DIR, APP_NAME, CONFIG_FILE)
		config = configparser.ConfigParser()
		config.read(CONFIG_PATH)
		BASE_API_URL = config['edc_sms']['base_api_url']

		INSTALLED_APPS = (
		  ...
		  'django_apscheduler',
		  'edc_sms.apps.AppConfig',
		)

		APSCHEDULER_DATETIME_FORMAT =  "N j, Y, f:s a"  # Default
	
	`project.conf` This is placed outside the project since it holds sensitive information
	
		[edc_sms]
		base_api_url = '' # This hold the HTTP api url

Run migrations:

