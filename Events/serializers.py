from rest_framework import serializers 
from .models import Event, Attendance


class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False)
    class Meta:
        model = Event 
        fields = '__all__'
        extra_kwargs = {
                'is_active':{'read_only':True},
                'has_ended':{'read_only':True}
        }

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'
        extra_kwargs = {
                'is_present':{'read_only':True},
                'clocked_in_at':{'read_only':True},
                'clocked_out_at':{'read_only':True}
        }

