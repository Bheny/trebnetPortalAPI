from django.db import models
from Profiles.models import Profile 
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from Notifications.services import send_notification
from .services import unique_request_id_generator

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=20,blank=True)
    sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.DO_NOTHING, null=False)
    reciever = models.ForeignKey(Profile, related_name="reciever", on_delete=models.DO_NOTHING, null=False)
    reference = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.transaction_id


@receiver(post_save, sender=Transaction)
def transaction_post_save(sender, instance, **kwargs):
    instance.transaction_id = unique_request_id_generator
    #subtracts amount sent from sender's balance
    instance.sender.balance -= instance.amount
    instance.sender.save()
    send_notification(f'You have sent {instance.amount} RCs to {instance.reciever}',instance.sender)
    #adds amount sent from sender's balance to receiver
    instance.reciever.balance += instance.amount
    instance.reciever.save()
    send_notification(f'You have recieved {instance.amount} RCs from {instance.sender}',instance.sender)
    