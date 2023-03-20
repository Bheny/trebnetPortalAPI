from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import PhoneBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','username','email','first_name','last_name','password') 
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'email','first_name','last_name','password')
        extra_kwargs = {
                       'password': {'write_only':True},
                       'first_name':{'required':True},
                       'last_name':{'required':True},
                       
                       }

    def create(self, validated_data):
        try:
            user = User.objects.create_user(username=validated_data['username'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'],
                                            email=validated_data['email'],
                                            password=validated_data['password'])
            return user
        except KeyError as e:
            return e

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField() 
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorect credentials Passed')




class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username']

        
class PhoneBookSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(max_length=20,required=False)
    class Meta:
        model = PhoneBook 
        fields = ['phone','otp']