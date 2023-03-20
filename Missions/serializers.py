from rest_framework import serializers 
from .models import Mission 
from Ranks.serializers import RankSerializer
from Profiles.serializers import ProfileSerializer 




class MissionSerializer(serializers.ModelSerializer):
    ranks = RankSerializer()
    class Meta:
        model = Mission 
        fields = '__all__'

    def create(self, validated_data):
        rank_data = validated_data.pop('ranks')
        print(rank_data)
        rank = Rank.objects.get(title=rank_data['title'])  # get the existing rank object
        
        mission = Mission.objects.create(**validated_data, rank=rank)
        return mission    


class MissionApplicationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    mission = MissionSerializer()
    class Meta:
        model = Mission 
        fields = '__all__'