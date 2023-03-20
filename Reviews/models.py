from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from django.db import  IntegrityError
from Profiles.models import Profile


class Review(models.Model):
    sender = models.ForeignKey(Profile, related_name="sender_profile", on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(Profile, related_name="receiver_profile", on_delete=models.DO_NOTHING)
    comment = models.TextField(blank=True)
    ratings = models.PositiveIntegerField(default=0)
    is_active= models.BooleanField(default=True)  
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} reviewed {}'.Format(self.sender,self.receiver)
