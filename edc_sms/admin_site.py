from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_header = 'Messages'
    site_title = 'Messages'
    index_title = 'Messages Administration'
    site_url = '/administration/'


edc_sms_admin = AdminSite(name='edc_sms_admin')
