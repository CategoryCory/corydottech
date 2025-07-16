from django.urls import path

from dev_log.views import DevLogEntryListView, DevLogEntryDetailView

app_name = 'dev_log'
urlpatterns = [
    path('', DevLogEntryListView.as_view(), name='dev_log-list'),
    path('<slug:slug>/', DevLogEntryDetailView.as_view(), name='dev_log-detail'),
]