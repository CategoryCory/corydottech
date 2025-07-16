import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from projects.models import Project


class DevLogEntry(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='dev_log_entries')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(help_text='The main content of the log entry. Markdown is supported.')
    published_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-published_date', )
        verbose_name = 'Dev Log Entry'
        verbose_name_plural = 'Dev Log Entries'

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = f'{slugify(self.title)}-{str(uuid.uuid4())[-12:]}'
        if self.status == 'published' and not self.published_date:
            self.published_date = timezone.now()
        super(DevLogEntry, self).save(*args, **kwargs)
