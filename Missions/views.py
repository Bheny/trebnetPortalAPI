from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Mission 
from .serializers import MissionSerializer, MissionApplicationSerializer

class MissionList(generics.GenericAPIView):
    """
    List all Missions or creates a new Mission"
    """
    serializer_class = MissionSerializer

    def get(self, request):
        #get the user Mission 
        Missions = Mission.objects.all()
        serializer = MissionSerializer(Missions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        print(serializer.is_valid())
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

    def get_queryset(self, request, pk):
        Mission = self.get_object(pk)
        serializer = MissionSerializer(Mission)
        return Response(serializer.data)

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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self, request, pk):
        Mission = self.get_object(pk)
        serializer = MissionApplicationSerializer(MissionApplication)
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

