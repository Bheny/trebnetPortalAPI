from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Notification 
from .serializers import *

class NotificationList(generics.GenericAPIView):
    """
    List all Notifications or creates a new Notification"
    """
    serializer_class = NotificationSerializer

    def get(self, request):
        #get the user Notification 
        Notifications = Notification.objects.all()
        serializer = NotificationListSerializer(Notifications, many=True)
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

    def get(self, request, pk):
        Notification = self.get_object(pk)
        serializer = NotificationListSerializer(Notification)
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

