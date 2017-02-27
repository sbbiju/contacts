from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    # ContactList,
    # ContactCreate,
    ContactDetail,
    ContactDelete,
    ContactUpdate,
    # MeetingList,
    MeetingDetail,
    # MeetingCreate,
    contact_list,
    meeting_list,
    MeetingUpdate,
    MeetingDelete,
    meeting_create,
    contact_create,
    search_contact,

    )


urlpatterns = [
    # url(r'^contact/$', ContactList.as_view(), name='contact_list'),
    url(r'^contact/$', contact_list, name='contact_list'),
    url(r'^contact/search/$', search_contact, name='search-contact'),
    # url(r'^contact/create/$', ContactCreate.as_view(), name='contact_create'),
    url(r'^contact/create/$', contact_create, name='contact_create'),
    url(r'^contact/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^contact/(?P<pk>\d+)/delete/$', ContactDelete.as_view(), name='contact_delete'),
    url(r'^contact/(?P<pk>\d+)/edit/$', ContactUpdate.as_view(), name='contact_edit'),

    # url(r'^meeting/$', MeetingList.as_view(), name='meeting_list'),
    url(r'^meeting/$', meeting_list, name='meeting_list'),
    url(r'^meeting/(?P<pk>\d+)/$', MeetingDetail.as_view(), name='meeting_detail'),
    # url(r'^meeting/create/$', MeetingCreate.as_view(), name='meeting_create'),
    url(r'^meeting/create/$', meeting_create, name='meeting_create'),
    url(r'^meeting/(?P<pk>\d+)/delete/$', MeetingDelete.as_view(), name='meeting_delete'),
    url(r'^meeting/(?P<pk>\d+)/edit/$', MeetingUpdate.as_view(), name='meeting_edit'),


]

