from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from Ranks.serializers import RankSerializer
# class UpdateProfileDetailSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     class Meta:
#         model = Profile
#         fields = ('id','user','bio','image','first_name','last_name')
#         depth = 1


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id','user','bio','image','is_driver','is_verified')
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','first_name','last_name','email','username')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rank = RankSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
