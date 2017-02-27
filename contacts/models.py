from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    first_name = models.CharField(max_length=80,blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    job_title = models.CharField(verbose_name='Job Title', max_length=120,  blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    company = models.CharField(verbose_name='Company', max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.first_name)

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs={'pk': self.pk})


class Meeting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    participant = models.CharField(verbose_name='Participants', max_length=120, blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=120, blank=True, null=True)
    # general_info = models.CharField(verbose_name='General Information', max_length=120, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    meeting_date =  models.DateField(default=datetime.date.today, verbose_name='Date')

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-meeting_date"]

    def get_absolute_url(self):
        return reverse('meeting_detail', kwargs={'pk': self.pk})

