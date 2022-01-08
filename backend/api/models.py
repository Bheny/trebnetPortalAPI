from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	location = models.CharField(max_length=200, blank=True, null=True)
	balance = models.DecimalField(max_digits=999,decimal_places=2,default=0)


	def __str__(self):
		return f'{self.user.username} Profile'  


	def get_alphabet(self):
		username = self.user.username
		return username[0]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=255, blank=False)
	image = models.ImageField(default='default.png', upload_to="projects", blank=True)
	timeline = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(Profile, related_name="author", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	

	def __str__(self):
		return self.title