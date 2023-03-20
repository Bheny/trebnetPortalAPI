from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id','last_login','username','first_name','last_name','password','email','is_staff','is_active','date_joined',)
		extra_kwargs = {'password': {'read_only':True}} #prevents editting of password directly from the user endpoint


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only':True}}

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
		return user

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError('Incorrect credentials passed')

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)