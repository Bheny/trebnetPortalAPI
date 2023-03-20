from rest_framework import serializers
from .models import Review

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 3

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # swagger_schema_fields = {
        #     'type': 'object',
        #     'properties': {
        #         'first_name': {
        #             'type': 'string',
        #             'description': 'First name of the user'
        #         },
        #         'last_name': {
        #             'type': 'string',
        #             'description': 'Last name of the user'
        #         },
        #         'bio': {
        #             'type': 'string',
        #             'description': 'User bio'
        #         },
        #         'avatar': {
        #             'type': 'file',
        #             'description': 'User avatar image'
        #         }
        #     }
        # }