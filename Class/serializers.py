from rest_framework import serializers 
from .models import Class 
from Profiles.models import ClassApplication

class ClassSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False)
    class Meta:
        model = Class 
        fields = '__all__'

class ClassApplicationSerializer(serializers.ModelSerializer):
    is_granted = serializers.BooleanField(default=False)
    completed = serializers.BooleanField(default=False)
    class Meta:
        model = ClassApplication 
        fields = '__all__'

