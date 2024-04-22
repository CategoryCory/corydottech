from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet

from jobs.models import Job
from projects.models import Project


def home(request) -> HttpResponse:
    projects: QuerySet[Project] = Project.objects.all()
    jobs: QuerySet[Job] = Job.objects.order_by('-start_date')
    context: dict[str, QuerySet] = {
        'projects': projects,
        'jobs': jobs,
    }
    return render(request, 'pages/home.html', context=context)
