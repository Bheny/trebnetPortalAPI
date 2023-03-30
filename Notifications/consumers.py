from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from djangochannelsrestframework.observer import ModelObserver
from .models import Notification
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.user = self.scope["user"]
        # if self.user.is_anonymous:
        #     await self.close()
        # else:
        #     await self.channel_layer.group_add(
        #         f"user_{self.user.id}",
        #         self.channel_name,
        #     )
        await self.channel_layer.group_add(
                f"user_",
                self.channel_name,
            )
        print("connection established",self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f"user_",
            self.channel_name,
        )

    async def send_comment_notification(self, instance=None):
        print("sending message: ")
        await self.send(text_data=f"New notifaication on ")

    async def receive(self, text_data):
        message = json.loads(text_data)
        # check that the WebSocket is still open
        
        print("Received message: ", message)
        self.send(text_data=f"New notifaication on ")
        self.send_comment_notification()
        
        

class NotificationObserver(ModelObserver):
    model = Notification
    queryset = Notification.objects.all()

    async def notify(self, instance, **kwargs):
        user = instance.profile.user
        channel_layer = get_channel_layer()
        group_name = f"user_{user.id}"
        message = {"type": "send_comment_notification", "data": "Comment Notification"}
        await channel_layer.group_send(group_name, message)






























# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     UpdateModelMixin,
#     DeleteModelMixin
# )
# from djangochannelsrestframework.observer import model_observer

# from .models import Notification
# from .serializers import NotificationSerializer


# class NotificationConsumer(
#     AsyncWebsocketConsumer,
#     ListModelMixin,
#     CreateModelMixin,
#     UpdateModelMixin,
#     DeleteModelMixin
# ):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer

#     async def connect(self):
#         print("connection established",dir(self))
#         await self.accept()

#     # async def disconnect(self, close_code):
#     #     pass

#     @action(detail=True, methods=['post'])
#     def subscribe(self, pk):
#         print("subscribe method has been accessed")
#         model_observer(self, Notification.objects.get(profile=pk))

#     @action()
#     def unsubscribe(self, pk):
#         model_observer(self, Notification.objects.get(pk=pk), remove=True)

#     @database_sync_to_async
#     def get_notification(self, notification_id):
#         try:
#             notification = Notification.objects.get(profile=notification_id)
#             return notification
#         except Notification.DoesNotExist:
#             pass
#         return None



# from .models import Notification 
# from.serializers import NotificationSerializer
# from djangochannelsrestframework.consumers import AsyncAPIConsumer
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
# from djangochannelsrestframework.observer import model_observer
# from djangochannelsrestframework.decorators import action
# from channels.db import database_sync_to_async

# # class NotificationConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
# class NotificationConsumer(GenericAsyncAPIConsumer):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer

#     @model_observer(Notification)
#     async def notification_activity(
#         self,
#         message: NotificationSerializer,
#         observer=None,
#         subscribing_request_ids=[],
#         **kwargs
#     ):
#         print("sending message")
#         await self.send_json(dict(message.data))

#     @notification_activity.serializer(NotificationSerializer)
#     def notification_activity(self, instance: Notification, action, **kwargs) -> NotificationSerializer:
#         """This will return the notification serializer"""
#         print("returning notification serializer")
#         return instance

#     # @action()
#     # async def subscribe_to_notification_activity(self, request_id, **kwargs):
#     #     print(dir(self.notification_activity))
#     #     await self.notification_activity.send(request_id=request_id)

#     @database_sync_to_async
#     def get_notifications(self):
#         print("getting notifications")
#         # This function returns all notifications that have a receiver field
#         # that matches the current user (assuming the current user is stored in self.scope['user'])
#         return Notification.objects.all() #filter(receiver=self.scope['user'])

#     @action()
#     async def subscribe_to_notifications(self, request_id, **kwargs):
#         print("subscribing to notification activity")
#         notifications = await self.get_notifications()
        
#         for notification in notifications:
#             await notification.subscribe(self.channel_name)
            
#         await self.send_response({'status': 'success', 'message': 'Subscribed to all notifications.'}, request_id=request_id)





# # # create an instance of MyConsumer and register the action method
# # my_consumer = NotificationConsumer()
# # my_consumer.add_action('subscribe_to_notification_activity', my_consumer.subscribe_to_notification_activity)