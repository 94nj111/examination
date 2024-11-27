from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
