import re
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import (
    ListboardFilterViewMixin, SearchFormViewMixin)
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ..model_wrappers import ContactModelWrapper


class ListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                    ListboardFilterViewMixin,
                    SearchFormViewMixin, ListboardView):

    listboard_template = 'contact_listboard_template'
    listboard_url = 'contact_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    model = 'edc_sms.contact'
    model_wrapper_cls = ContactModelWrapper
    navbar_name = 'edc_sms'
    navbar_selected_item = 'contact'
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'contact_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            contact_add_url=self.model_cls().get_absolute_url())
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
