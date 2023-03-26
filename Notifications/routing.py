from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/notifications/$", consumers.NotificationConsumer.as_asgi()),
]




# application = ProtocolTypeRouter({
#     'websocket': URLRouter(websocket_urlpatterns),
# })





# from django.urls import path, re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path('ws/notification/$', consumers.NotificationConsumer.as_asgi()),
# ]
