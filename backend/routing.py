from django.urls import re_path

from Notifications import consumers
from Chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
    re_path(r'ws/chat/', ChatConsumer.as_asgi()),
]

