from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Class
from .serializers import ClassSerializer

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

    def post(self, request):
        # create class 
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)