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
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    xp = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_verified = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    def get_current_rank(self):
        return self.rank
        

@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    # on create of user account, check if there is an existing profile.
    # if it exists dont create another .
 
    if created:
        rank, rank_created = Rank.objects.get_or_create(title="Associate", active=True)
        instance.rank = rank 
        instance.save()
      
        

    
   
    
        
       


@receiver(post_save, sender=Profile)
def profile_post_save(sender, instance, **kwargs):
    print("after",instance.rank)


class ClassApplication(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    is_granted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Request for {} by {}'.format(self.Class.title, self.profile.user.username)

