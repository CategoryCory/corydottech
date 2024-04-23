import uuid
from django.db import models
from django.utils.text import slugify

from taggit.managers import TaggableManager


class Project(models.Model):
    COMPLETE = 'complete'
    IN_PROGRESS = 'in_progress'

    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (IN_PROGRESS, 'In Progress'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=IN_PROGRESS)
    skills_used = TaggableManager()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{uuid.uuid4()}'
        super(Project, self).save(*args, **kwargs)
