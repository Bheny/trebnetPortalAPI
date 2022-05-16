from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

RANKS = (
		('8','Cadet - Level 1'),
		('7','Cadet - Level 2'),
		('6','Cadet - Level 3'),
		('5','Cadet - Level 4'),
		('4','Lieutenant'),
		('3','Captain'),
		('2','Major'),
		('1','General'),
		('0','Class S'),

		)
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	location = models.CharField(max_length=200, blank=True, null=True)
	balance = models.DecimalField(max_digits=999,decimal_places=2,default=0)
	rank = models.CharField(choices=RANKS, max_length=255, default="1")

	def is_cleared(self):
		if int(self.rank) < 4:
			return True
		return False

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
	rank = models.CharField(choices=RANKS, max_length=255, default="4")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	

	def __str__(self):
		return self.title


class Team(models.Model):
	image = models.ImageField(default="default.png", upload_to="Teams")
	name = models.CharField(max_length=255)
	members = models.ManyToManyField(Profile, related_name="team_members", blank="True")
	description = models.TextField(blank=True)
	projects = models.ManyToManyField(Project, related_name="team_projects", blank=True)
	rank = models.CharField(choices=RANKS, max_length=255, default="4")
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Team {}'.format(self.name)


class Job(models.Model):
	
	image = models.ImageField(default="default.png",upload_to="jobs", blank=True)
	title = models.CharField(max_length=255)
	max_personel = models.PositiveIntegerField(default=0)
	min_personel = models.PositiveIntegerField(default=0)
	rank = models.CharField(choices=RANKS, max_length=255, default="4")

	def __str__(self):
		return '{} request for {}'.format(self.rank,self.title)


class Transaction(models.Model):
	transaction_id = models.CharField(max_length=20)
	sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.DO_NOTHING, null=False)
	reciever = models.ForeignKey(Profile, related_name="reciever", on_delete=models.DO_NOTHING, null=False)
	amount = models.PositiveIntegerField(default=0)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.transaction_id

class Event(models.Model):
	image = models.ImageField(default="default.png",upload_to="events",blank=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	location = models.CharField(max_length=255)
	date_time = models.DateTimeField()
	attendants = models.ManyToManyField(Profile, related_name="participants", blank=True)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Question(models.Model):
	image = models.ImageField(default="default.png",upload_to="events",blank=True)
	subject = models.CharField(max_length=255)
	answer = models.TextField()
	answered_by = models.ForeignKey(User, related_name="answered_by", on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.subject)


class Idea(models.Model):
	image = models.ImageField(default="default.png",upload_to="events",blank=True)
	title = models.CharField(max_length=255, blank=True)
	description = models.TextField()
	posted_by = models.CharField(max_length=255, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class News(models.Model):
	image = models.ImageField(default="default.png",upload_to="events",blank=True)
	title = models.CharField(max_length=255, blank=True)
	description = models.TextField()
	posted_by = models.CharField(max_length=255, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Announcement(models.Model):
	image = models.ImageField(default="default.png",upload_to="events",blank=True)
	title = models.CharField(max_length=255, blank=True)
	description = models.TextField()
	posted_by = models.CharField(max_length=255, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title