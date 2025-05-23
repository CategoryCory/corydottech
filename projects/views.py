from typing import Any
from django.views.generic.detail import DetailView

from .models import Project


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=self.kwargs['slug'])
        return context
