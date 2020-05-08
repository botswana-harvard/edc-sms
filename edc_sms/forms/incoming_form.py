from django import forms

from ..models import Incoming


class IncomingForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Incoming
        fields = '__all__'
