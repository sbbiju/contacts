from django import forms

from .models import Contact, Meeting


class MeetForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ['title', 'participant', 'notes', 'meeting_date']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'job_title', 'email', 'company', 'notes']