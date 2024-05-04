from django.urls import path

from .views import ProjectDetailView

app_name = 'projects'
urlpatterns = [
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]
