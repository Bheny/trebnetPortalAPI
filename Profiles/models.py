from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from Class.models import Class
from Ranks.models import Rank




class Profile(models.Model):
    image = models.ImageField(upload_to='images/profile/', blank=True)
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    rank = models.ForeignKey(Rank, related_name="profile_rank", on_delete=models.CASCADE)
    Class = models.ManyToManyField(Class, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_verified = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    rank, rank_created = Rank.objects.get_or_create(title="Associate", active=True)
    if created:
        Profile.objects.create(user=instance, rank=rank, is_verified=False)



class Application(models.Model):
    applicant  = models.ForeignKey(Profile, related_name="applicant_profile", on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} is requesting for Driver Verification..'.format(self.applicant.user.username)