from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Class
from .serializers import ClassSerializer, ClassApplicationSerializer
from Profiles.models import ClassApplication
class ClassList(generics.GenericAPIView):
    """
    List all Ranks or creates a new Class"
    """
    serializer_class = ClassSerializer

    def get(self, request):
        #get the user rank 
        Classes = Class.objects.all()
        serializer = ClassSerializer(Classes, many=True)
        return Response(serializer.data)
    
    # def post(self, request):
    #     # create class 
    #     serializer = ClassSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassDetail(generics.GenericAPIView):
    serializer_class = ClassSerializer

    def get_object(pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404
        

    def get(self, request, pk):
        Class = self.get_object(pk)
        serializer = ClassSerializer(Class)
        return Response(serializer.data)
    
    def get_queryset(self, request, pk):
        Class = self.get_object(pk)
        serializer = ClassSerializer(Class)
        return Response(serializer.data)
      

class ClassApplicationList(generics.GenericAPIView):
    """
    List all Classes "
    """
    serializer_class = ClassApplicationSerializer

    def get(self, request):
        #get the user rank 
        ClassApplications = ClassApplication.objects.all()
        serializer = ClassApplicationSerializer(ClassApplications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class ClassApplicationDetail(generics.GenericAPIView):
    serializer_class = ClassApplicationSerializer

    def get_object(pk):
        try:
            return ClassApplications.objects.get(pk=pk)
        except ClassApplications.DoesNotExist:
            raise Http404
        

    def get(self, request, pk):
        ClassApplication = self.get_object(pk)
        serializer = ClassApplicationSerializer(Class)
        return Response(serializer.data)
    
    def get_queryset(self, request, pk):
        ClassApplication = self.get_object(pk)
        serializer = ClassApplicationSerializer(Class)
        return Response(serializer.data)

    