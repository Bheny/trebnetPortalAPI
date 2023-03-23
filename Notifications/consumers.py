import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "notifications"

        #join to group 
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()



        # await self.accept()
        # self.id = self.scope["path"] #["kwargs"]["id"]
        # print(str(self.scope))
        # # Subscribe the user to their notifications 
        # await self.channel_layer.group_add(
        #     self.id,
        #     self.channel_name
        # )
    
    async def disconnect(self):
        # Unsubscribe the from their notifications
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def recieve(self, texxt_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        event =  {
            'type':'send_message',
            'message':message
        }

        await self.channel_layer.group_send(self.group_name, event)
    
    async def send_message(self, event):
        notification = event['message']

        #Send the notification to the client
        await self.send(text_data=json.dumps({
            'message':message
        }))