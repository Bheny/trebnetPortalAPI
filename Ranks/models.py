from django.db import models

# Create your models here.
class Rank(models.Model):
    title = models.CharField(max_length=100, unique=True)
    tag = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
