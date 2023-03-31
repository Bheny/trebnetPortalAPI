from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Notification 
from .serializers import *
from django.shortcuts import render, reverse
from rest_framework.decorators import action
from rest_framework import viewsets
from channels.layers import get_channel_layer
from djangochannelsrestframework.decorators import action as ws_action

def index(request):
    return render(request, 'index2.html')



class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_create(self, serializer):
        notification = serializer.save() 
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications", {"type": "notification.created", "notification": notification}
        )
    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        user = request.user
        # notification = self.get_object()
        # notification.users.add(user)
        # notification.save()
        return Response({'status': user})

    @action(detail=True, methods=['post'])
    def unsubscribe(self, request, pk=None):
        user = request.user
        notification = self.get_object()
        notification.users.remove(user)
        notification.save()
        return Response({'status': 'unsubscribed'})

    @ws_action(detail=True)
    async def send_notification(self, request, pk=None):
        notification = self.get_object()
        notification.send()
        return Response({'status': 'sent'})


class NotificationList(generics.GenericAPIView):
    """
    List all Notifications or creates a new Notification"
    """
    serializer_class = NotificationSerializer

    def get(self, request):
        #get the user Notification 
        Notifications = Notification.objects.all()
        serializer = NotificationSerializer(Notifications, many=True)
        return Response(serializer.data)

    def get_queryset(self, request, pk):
        Notification = self.get_object(pk)
        serializer = NotificationSerializer(Notification)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Notification instance.
    """
    serializer_class = NotificationSerializer
    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404

    def queryset(self, request,):
        pass 
    
    def get(self, request, pk):
        Notification = self.get_object(pk)
        serializer = NotificationSerializer(Notification)
        return Response(serializer.data)

    def put(self, request, pk):
        Notification = self.get_object(pk)
        serializer = NotificationSerializer(Notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        Notification = self.get_object(pk)
        Notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

