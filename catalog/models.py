from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="teg_task",
        blank=True
    )
    def __str__(self):
        return self.name
