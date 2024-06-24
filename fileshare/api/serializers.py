from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import file, User

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_ops_user', 'is_client_user', 'groups', 'user_permissions']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = file
        fields = ['file', 'uploaded_at']
