from django.db import models

from taggit.managers import TaggableManager


class Project(models.Model):
    COMPLETE = 'complete'
    IN_PROGRESS = 'in_progress'

    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (IN_PROGRESS, 'In Progress'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=IN_PROGRESS)
    skills_used = TaggableManager()

    def __str__(self) -> str:
        return self.name
