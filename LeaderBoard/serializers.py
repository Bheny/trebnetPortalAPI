from rest_framework import serializers 
from .models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    # rank = serializers.CharField(max_length=100)    
    class Meta:
        model = Transaction
        fields = '__all__'
        depth=2
       

class TransactionSerializer(serializers.ModelSerializer):
    # rank = serializers.CharField(max_length=100)    
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {
                'transaction_id':{'read_only':True},
               
        }

    