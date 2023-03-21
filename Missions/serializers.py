from rest_framework import serializers 
from .models import Mission , MissionApplication
from Ranks.serializers import RankSerializer
from Ranks.models import Rank
from Profiles.serializers import ProfileSerializer 


class MissionListSerializer(serializers.ModelSerializer):
    # rank = serializers.CharField(max_length=100)    
    class Meta:
        model = Mission 
        fields = '__all__'
        depth=1

class MissionSerializer(serializers.ModelSerializer):
    # rank_id = serializers.CharField(max_length=100)    
    class Meta:
        model = Mission 
        fields = '__all__'
        

    def create(self, validated_data):
        # rank_id = validated_data.pop('rank')
        # print(validated_data, rank_id)
        # rank = Rank.objects.get(pk=rank_id)  # get the existing rank object
        mission = Mission.objects.create(**validated_data)
        return mission    


class MissionApplicationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MissionApplication 
        fields = '__all__'
        depth=3

class MissionApplicationSerializer(serializers.ModelSerializer):
    # profile = serializers.CharField(max_length=20)
    # mission = serializers.CharField(max_length=20)
    class Meta:
        model = MissionApplication 
        fields = '__all__'
        extra_kwargs = {
                'is_assigned':{'read_only':True},
                'completed':{'read_only':True},
                'completed_at':{'read_only':True}
        }

    # def create(self, validated_data):
    #     profile = validated_data.pop('profile')
    #     mission = validated_data.pop('mission')
    #     profile = Profile.objects.get(pk=profile.id)
    #     mission = Mission.objects.get(pk=mission.id)

    #     missionApplication = MissionApplication.objects.create(**validated_data, mission=mission_data, profile=profile_data)
    #     return missionApplication