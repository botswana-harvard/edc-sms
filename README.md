[![Build Status](https://travis-ci.org/botswana-harvard/edc-sms.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-sms.svg?branch=develop) [![Coverage Status](https://coveralls.io/repos/github/botswana-harvard/edc-sms/badge.svg?branch=develop)](https://coveralls.io/github/botswana-harvard/edc-sms?branch=develop)

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
		
		DASHBOARD_URL_NAMES = {
			...
		    'contact_listboard_url': 'contact_listboard_url',
		}
		
		
		DASHBOARD_BASE_TEMPLATES = {
			....
		    'listboard_base_template': 'edc_sms/base.html',
		    'contact_listboard_template': 'edc_sms/listboard.html',
		}
	
	`project.conf` This is placed outside the project since it holds sensitive information
	
		[edc_sms]
		base_api_url = '' # This hold the HTTP api url

Run migrations:

