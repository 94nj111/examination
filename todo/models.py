from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def get_absolute_url(self):
        return reverse("todo:tag-detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
    
    def get_absolute_url(self):
        return reverse("todo:task-detail", kwargs={"pk": self.pk})
    
