from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer, ProfileDetailSerializer #UpdateProfileDetailSerializer
from rest_framework import viewsets, generics, permissions, serializers, filters

class ProfileList(generics.GenericAPIView):
    """
    List all Profiles or create a new Profile.
    """
    serializer_class = ProfileSerializer
    def get(self, request):
        # get the user profile for the authenticated user
        Profiles = Profile.objects.all()
        serializer = ProfileDetailSerializer(Profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UpdateProfileDetail(generics.GenericAPIView):
#     """
#    Update a Profile instance.
#     """
#     serializer_class = UpdateProfileDetailSerializer
#     def get_object(self, pk):
#         try:
#             return Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             raise Http404


#     def update_user(self, pk, first_name, last_name):
#         Profile = self.get_object(pk)
#         Profile.user.first_name = first_name
#         Profile.user.last_name = last_name
#         Profile.user.save()
#         print(Profile.user.first_name)
#         return True 

#     def put(self, request, pk):
#         Profile = self.get_object(pk)
#         serializer = ProfileDetailSerializer(Profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(request.data)
#             self.update_user(pk,request.data['first_name'],request.data['last_name'])
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Profile instance.
    """
    serializer_class = ProfileSerializer
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile)
        return Response(serializer.data)

    def get_queryset(self, request, pk):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile)
        return Response(serializer.data)

    def put(self, request, pk):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        Profile = self.get_object(pk)
        Profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


