from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Rank 
from .serializers import RankSerializer

class RankList(generics.GenericAPIView):
    """
    List all Ranks or creates a new Rank"
    """
    serializer_class = RankSerializer

    def get(self, request):
        #get the user rank 
        Ranks = Rank.objects.all()
        serializer = RankSerializer(Ranks, many=True)
        return Response(serializer.data)


class RankDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Rank instance.
    """
    serializer_class = RankSerializer
    def get_object(self, pk):
        try:
            return Rank.objects.get(pk=pk)
        except Rank.DoesNotExist:
            raise Http404

    def get_queryset(self, request, pk):
        Rank = self.get_object(pk)
        serializer = RankSerializer(Rank)
        return Response(serializer.data)

    def put(self, request, pk):
        Rank = self.get_object(pk)
        serializer = RankSerializer(Rank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            # self.update_user(pk,request.data['first_name'],request.data['last_name'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        Rank = self.get_object(pk)
        Rank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

