from django.test import TestCase
from channels.testing  import WebsocketCommunicator
from django.test import LiveServerTestCase
from django.contrib.auth.models import User 
from .models import Notification 
from .consumers import NotificationConsumer
from asgiref.sync import async_to_sync, sync_to_async

class NotificationTest(LiveServerTestCase):
    async def test_notification_are_sent_to_users(self):
        
        @sync_to_async
        def get_user(self):
            # create a user to recieve notifications
            user = User.objects.create(username='testuser', email='testuser@gmail.com', password='thedemonfox30')
            self.client.login(username="testuser", password='testpass')
            
            return user #User.objects.get(username='admin')

        user = {'id':1}
           
        # connect to the notification consuner
        communicator = WebsocketCommunicator(NotificationConsumer.as_asgi(), f'/notifcations/1')
            
        
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        #send a notification to the user
        notification = {'title':'Test notification','profile':user,'message':'This is annother test notification'}
        await communicator.send_json_to(notification)

        #Check that the user recieved the notification
        reponse  = await  communicator.receive_json_from()
        self.assertEqual(response, notification)

        # Disconnect from the notification consumer 
        await communicator.disconnect()