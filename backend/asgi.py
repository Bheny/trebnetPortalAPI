"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
# from channels.security.websocket import AllowedHostOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter

from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
     'websocket': 
        URLRouter(websocket_urlpatterns )
    , 
    
    
    
    
    #URLRouter(routing.websocket_urlpatterns), #AuthMiddlewareStack(
    #     URLRouter(
    #         Notification.routing.websocket_urlpatterns
    #     )
    # )
})
