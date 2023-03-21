from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Event 
from .serializers import *
from Profiles.models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class EventFilter(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']

class EventSearch(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']

    
class EventList(generics.GenericAPIView):
    """
    List all Events or creates a new Event"
    """
    serializer_class = EventSerializer

    def get(self, request):
        #get the user Event 
        Events = Event.objects.all()
        serializer = EventListSerializer(Events, many=True)
        return Response(serializer.data)

    def get_queryset(self, request, pk):
        Event = self.get_object(pk)
        serializer = EventSerializer(Event)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Event instance.
    """
    serializer_class = EventSerializer
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Event = self.get_object(pk)
        serializer = EventListSerializer(Event)
        return Response(serializer.data)

    def put(self, request, pk):
        Event = self.get_object(pk)
        serializer = EventSerializer(Event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        Event = self.get_object(pk)
        Event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AttendanceList(generics.GenericAPIView):
    """
    List all Attendance or creates a new Event"
    """
    serializer_class = AttendanceSerializer

    def get(self, request):
        #get the user Event 
        Attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(Attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
                
                profile = serializer.validated_data['profile']
                Event= serializer.validated_data['Event']
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            print("try stated")
            profile = Profile.objects.get(pk=profile.id)
            rank = Event.objects.get(pk=Event.id).rank
            if profile.rank.score < rank.score:
                return Response(f'You need rank {rank} or higher to attend this Event')
            else:
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Profile.DoesNotExist:
            raise Http404
        
        except Rank.DoesNotExist:
            raise Http404

# class AttendanceDetail(generics.GenericAPIView):
#     """
#     Retrieve, update or delete a Event instance.
#     """
#     serializer_class = AttendanceSerializer
#     def get_object(self, pk):
#         try:
#             return Attendance.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         Attendance = self.get_object(pk)
#         serializer = AttendanceListSerializer(Attendance)
#         return Response(serializer.data)

#     def get_queryset(self, request, pk):
#         Attendance = self.get_object(pk)
#         serializer = AttendanceListSerializer(Attendance)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         Attendance = self.get_object(pk)
#         serializer = AttendanceSerializer(Attendance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(request.data)
#             # self.update_user(pk,request.data['first_name'],request.data['last_name'])
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         Attendance = self.get_object(pk)
#         Attendance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

