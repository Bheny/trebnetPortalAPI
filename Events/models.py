from django.db import models
from Profiles.models import Profile
from Ranks.models import Rank
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from Notifications.services import send_notification


class Event(models.Model):
    image = models.ImageField(default="default.png",upload_to="events",blank=True)
    title = models.CharField(max_length=255)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    xp = models.PositiveIntegerField(default=0)
    date_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    has_ended = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

@receiver(post_save, sender=Event)
def Event_post_save(sender, instance, **kwargs):
    profiles = Profile.objects.filter(rank=instance.rank)
    for profile in profiles:
        send_notification(f'New Events for All {instance.rank} Rank and above!!!',profile)



class Attendance(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    clocked_in_at = models.TimeField(auto_now=True)
    clocked_out_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member.username} was at {self.event.title}'

@receiver(post_save, sender=Attendance)
def Attendance_post_save(sender, instance, **kwargs):
    if instance.event.is_active:
        instance.member.xp += instance.event.xp
        instance.member.save()
    

