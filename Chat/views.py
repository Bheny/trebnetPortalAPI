from rest_framework import viewsets
from .models import Room, Message, Forum, Thread, Post
from .serializers import RoomSerializer, MessageSerializer, ForumSerializer, ThreadSerializer, PostSerializer
from Profiles.serializers import ProfileSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"room_{serializer.validated_data['room'].id}",
            {
                "type": "chat.message",
                "message": serializer.data
            }
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = RoomSerializer