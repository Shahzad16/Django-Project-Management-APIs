from rest_framework import serializers
from .models import User, Project, Task

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data.get("role", "Member"),
        )
        user.set_password(validated_data["password"])  # Hash password
        user.save()
        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description'] 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
