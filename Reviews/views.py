from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from rest_framework import generics

class ReviewList(generics.GenericAPIView):
    """
    List all Reviews or create a new Review.
    """
    serializer_class = ReviewSerializer
    def get(self, request):
        # get the user Review for the authenticated user
        Reviews = Review.objects.all()
        serializer = ReviewSerializer(Reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):
    """
    Retrieve, update or delete a Review instance.
    """
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Review = self.get_object(pk)
        serializer = ReviewSerializer(Review)
        return Response(serializer.data)

    def put(self, request, pk):
        Review = self.get_object(pk)
        serializer = ReviewSerializer(Review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Review = self.get_object(pk)
        Review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
