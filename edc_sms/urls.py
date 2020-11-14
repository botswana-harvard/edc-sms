"""edc_sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.apps import apps as django_apps

from edc_dashboard import UrlConfig


from django.contrib import admin
from .admin_site import edc_sms_admin
from .views import HomeView, ListBoardView

app_name = 'edc_sms'
app_config = django_apps.get_app_config(app_name)

urlpatterns = [
    path('admin/', edc_sms_admin.urls),
    path('', HomeView.as_view(), name='home_url'),
    path('djangoq_admin/', admin.site.urls),
]

contact_listboard_url_config = UrlConfig(
    url_name='contact_listboard_url',
    view_class=ListBoardView,
    label='contact_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=app_config.identifier_pattern)

urlpatterns += contact_listboard_url_config.listboard_urls
