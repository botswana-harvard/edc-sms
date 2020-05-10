from django import forms

from ..models import Outgoing


class OutgoingForm(forms.ModelForm):

    class Meta:
        model = Outgoing
        fields = '__all__'
