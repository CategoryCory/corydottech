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
    slug = models.SlugField(max_length=150, blank=True, null=True, unique=True)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=IN_PROGRESS)
    github_url = models.URLField(blank=True, null=True)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    skills_used = TaggableManager()

    @property
    def date_str(self) -> str:
        dt = self.begin_date.strftime('%b %Y')
        if self.status == self.IN_PROGRESS:
            dt += ' \u2013 PRESENT'
        else:
            if self.end_date is not None:
                dt += f' \u2013 {self.end_date.strftime("%b %Y")}'

        return dt

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{str(uuid.uuid4())[-12:]}'
        super(Project, self).save(*args, **kwargs)
