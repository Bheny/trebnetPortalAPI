from rest_framework import generics, status 
from rest_framework.response import Response 
from .models import Transaction 
from .serializers import TransactionListSerializer, TransactionSerializer
from .services import auditor

class TransactionList(generics.GenericAPIView):
    """
    List all Transactions or creates a new Transaction"
    """
    serializer_class = TransactionSerializer

    def get(self, request):
        #get the user Transaction 
        Transactions = Transaction.objects.all()
        serializer = TransactionListSerializer(Transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            verified = auditor(serializer.validated_data)
            print(verified)
            if verified['status']: 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(verified)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class TransactionDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a Transaction instance.
    """
    serializer_class = TransactionListSerializer
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get_queryset(self, request, pk):
        Transaction = self.get_object(pk)
        serializer = TransactionListSerializer(Transaction)
        return Response(serializer.data)

    def get(self, request, pk):
        Transaction = self.get_object(pk)
        serializer = TransactionListSerializer(Transaction)
        return Response(serializer.data)
