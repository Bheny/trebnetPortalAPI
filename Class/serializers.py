from rest_framework import serializers 
from .models import Class 

class ClassSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False)
    class Meta:
        model = Class 
        fields = '__all__'