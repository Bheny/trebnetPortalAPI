from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Mission 
from .serializers import *
from Profiles.models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MissionFilter(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rank__title','points','is_active']

class MissionSearch(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']

    
class MissionList(generics.GenericAPIView):
    """
    List all Missions or creates a new Mission"
    """
    serializer_class = MissionSerializer

    def get(self, request):
        #get the user Mission 
        Missions = Mission.objects.all()
        serializer = MissionListSerializer(Missions, many=True)
        return Response(serializer.data)

    def get_queryset(self, request, pk):
        Mission = self.get_object(pk)
        serializer = MissionSerializer(Mission)
        return Response(serializer.data)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MissionDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Mission instance.
    """
    serializer_class = MissionSerializer
    def get_object(self, pk):
        try:
            return Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Mission = self.get_object(pk)
        serializer = MissionListSerializer(Mission)
        return Response(serializer.data)

    def queryset(self, request,):
        pass 
    
    def put(self, request, pk):
        Mission = self.get_object(pk)
        serializer = MissionSerializer(Mission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        Mission = self.get_object(pk)
        Mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MissionApplicationList(generics.GenericAPIView):
    """
    List all Missions or creates a new Mission"
    """
    serializer_class = MissionApplicationSerializer

    def get(self, request):
        #get the user Mission 
        Missions = MissionApplication.objects.all()
        serializer = MissionApplicationSerializer(MissionsApplication, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MissionApplicationSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
                
                profile = serializer.validated_data['profile']
                mission= serializer.validated_data['mission']
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            print("try stated")
            profile = Profile.objects.get(pk=profile.id)
            rank = Mission.objects.get(pk=mission.id).rank
            if profile.rank.score < rank.score:
                return Response(f'You need rank {rank} or higher to apply for this mission')
            else:
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Profile.DoesNotExist:
            raise Http404
        
        except Rank.DoesNotExist:
            raise Http404

class MissionApplicationDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Mission instance.
    """
    serializer_class = MissionApplicationSerializer
    def get_object(self, pk):
        try:
            return MissionApplication.objects.get(pk=pk)
        except Mission.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        MissionApplication = self.get_object(pk)
        serializer = MissionApplicationListSerializer(MissionApplication)
        return Response(serializer.data)

    def queryset(self, request,):
        pass 

    def get(self, request, pk):
        MissionApplication = self.get_object(pk)
        serializer = MissionApplicationListSerializer(MissionApplication)
        return Response(serializer.data)

    def put(self, request, pk):
        MissionApplication = self.get_object(pk)
        serializer = MissionApplicationSerializer(MissionApplication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        MissionApplication = self.get_object(pk)
        MissionApplication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

