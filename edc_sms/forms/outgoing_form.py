from django import forms

from ..models import Outgoing


class OutgoingForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Outgoing
        fields = '__all__'
