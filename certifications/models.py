from django.db import models
from taggit.managers import TaggableManager


class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    source = models.CharField(max_length=100, blank=True, null=True)
    date_earned = models.DateField()
    skills_used = TaggableManager()

    def __str__(self) -> str:
        return self.name
