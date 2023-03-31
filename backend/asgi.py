"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter
from .middleware import TokenAuthMiddleware

from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
     'websocket': 
        TokenAuthMiddleware(
            URLRouter(websocket_urlpatterns)
        
    ),
})
