from django.db import models
from django.contrib.auth.models import User
from Profiles.models import Profile
from Ranks.models import Rank
from Notifications.services import send_notification
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 


class Mission(models.Model):
    title = models.CharField(max_length=255)
    rank  = models.ForeignKey(Rank, on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='missions/', blank=True)
    points = models.IntegerField(default=0)
    xp = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}- {}'.format(self.title, self.rank)

@receiver(post_save, sender=Mission)
def Mission_post_save(sender, instance, **kwargs):
    profiles = Profile.objects.filter(rank=instance.rank)
    for profile in profiles:
        send_notification(f'New Mission for All {instance.rank} ranks and above!!!',profile)



class MissionApplication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Request for {} by {}'.format(self.mission.title, self.profile.user.username)

    def save(self, *args, **kwargs):
        # do something before saving
        if self.is_assigned:
            message = "Your Request for this mission has been Approved. Click to check details"
            send_notification(message,self.profile)
            if self.completed and self.mission.is_active:
                # automatically add the xp point allocated to a mission to the xp of the users who complete the task while its still active
                self.profile.xp += self.mission.xp 
                
        super().save(*args, **kwargs)
        # do something after saving