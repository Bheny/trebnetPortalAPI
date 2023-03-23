from rest_framework import serializers
from .models import Room, Message, Forum, Thread, Post
from Profiles.serializers import ProfileSerializer

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Message
        fields = '__all__'

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum 
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread 
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post 
        fields = '__all__'