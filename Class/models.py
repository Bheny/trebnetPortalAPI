from django.db import models


class Class(models.Model):
    image = models.ImageField(upload_to="class/", blank=True)
    title= models.CharField(max_length=100)
    description= models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

