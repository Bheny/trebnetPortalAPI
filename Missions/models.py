from django.db import models
from django.contrib.auth.models import User
from Profiles.models import Profile
from Ranks.models import Rank

class Mission(models.Model):
    title = models.CharField(max_length=255)
    ranks  = models.ManyToManyField(Rank)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='missions/', blank=True)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.title,self.ranks)

class MissionApplication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Request for {} by {}'.format(self.mission.title, self.profile.user.username)

