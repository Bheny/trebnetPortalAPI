from .models import Notification 
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from Profiles.models import Profile 
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Notification)
def send_notifications(sender, instance, **kwargs):
    """
        Send notifications to all connected clients via websockets
    """

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification", {
            "id":instance.id,
            'profile':instance.profile,
            'read':instance.read,
            'created_at': instance.created_at
        }
    )

def send_notification(message,reciever):
    notification = Notification.objects.create(message=message,profile=reciever)
    return notification

@receiver(pre_save, sender=Profile)
def profile_pre_save(sender, instance, **kwargs):
    try:
        previous = Profile.objects.get(id=instance.id)
        print("Before",previous.rank)
        if previous.rank != instance.rank:
            message = f'You have been promoted to {instance.rank}'
            send_notification(message, instance)
    except Profile.DoesNotExist:
        pass



