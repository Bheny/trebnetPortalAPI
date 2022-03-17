from rest_framework.serializers import ModelSerializer 

from django.contrib.auth.models import User  

class UserSerializer(ModelSerializer):

	class Meta:
		model = User 
		fields = ('last_login','username','first_name','last_name','email','is_staff','is_active','date_joined',)

