from django.views.generic import ListView, DetailView

from dev_log.models import DevLogEntry


class DevLogEntryListView(ListView):
    model = DevLogEntry
    ordering = ('-published_date', )


class DevLogEntryDetailView(DetailView):
    model = DevLogEntry
