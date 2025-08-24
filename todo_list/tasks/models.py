from django.db import models
from django.db.models import ManyToManyField

from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo:tag-list')


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = ManyToManyField(Tag, related_name='tasks', blank=True)

    class Meta:
        ordering = ['is_done', '-created_at']

    def __str__(self):
        return self.content[:50]

    def get_absolute_url(self):
        return reverse('todo:task-list')