from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar

edc_sms = Navbar(name='edc_sms')
no_url_namespace = True if settings.APP_NAME == 'edc_sms' else False

edc_sms.append_item(
    NavbarItem(name='edc_sms',
               label='EDC SMS',
               fa_icon='fa-cogs',
               url_name='edc_sms:home_url'))

edc_sms.append_item(
    NavbarItem(
        name='contact',
        title='Contact',
        label='Contact',
        fa_icon='fa fa-file-export',
        url_name=settings.DASHBOARD_URL_NAMES[
            'contact_listboard_url'],
        no_url_namespace=no_url_namespace))


site_navbars.register(edc_sms)
