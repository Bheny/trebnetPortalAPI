from channels.generic.websocket import AsyncWebsocketConsumer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DeleteModelMixin
)
from djangochannelsrestframework.observer import model_observer

from .models import Notification
from .serializers import NotificationSerializer


class NotificationConsumer(
    AsyncWebsocketConsumer,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DeleteModelMixin
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    # async def connect(self):
    #     await self.accept()

    # async def disconnect(self, close_code):
    #     pass

    @action()
    def subscribe(self, pk):
        model_observer(self, Notification.objects.get(pk=pk))

    @action()
    def unsubscribe(self, pk):
        model_observer(self, Notification.objects.get(pk=pk), remove=True)
