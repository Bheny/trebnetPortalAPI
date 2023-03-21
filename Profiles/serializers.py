from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from Ranks.serializers import RankSerializer
from Ranks.models import Rank
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
        fields = ('id','user','bio','image','is_verified','Class')
        depth = 3

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','first_name','last_name','email','username')

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # rank = RankSerializer()
    class Meta:
        model = Profile
        fields = ('user','bio','Class','rank')
        extra_kwargs = {
            "rank":{'read_only':True},
        }
        
    def create(self, validated_data):
        rank, created = Rank.objects.get_or_create(title="Associate", active=True)
        profile = Profile.objects.create(**validated_data, rank=rank)
        return profile 
