from django.db import models

from taggit.managers import TaggableManager


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=16)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills_used = TaggableManager()

    @property
    def is_current(self) -> bool:
        return self.end_date is None

    def __str__(self) -> str:
        return self.title
