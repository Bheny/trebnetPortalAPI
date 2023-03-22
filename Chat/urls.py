from django.urls import path, include
from rest_framework import routers
from .views import  RoomViewSet, MessageViewSet, ForumViewSet, ThreadViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'Forum',ForumViewSet)
router.register(r'Thread',ThreadViewSet)
router.register(r'Post',PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
