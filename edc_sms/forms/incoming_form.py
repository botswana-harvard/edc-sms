from django import forms

from ..models import Incoming


class IncomingForm(forms.ModelForm):

    class Meta:
        model = Incoming
        fields = '__all__'
