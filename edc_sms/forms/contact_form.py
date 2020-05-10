from django import forms

from ..models import Contact


class ContactForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Contact
        fields = '__all__'
