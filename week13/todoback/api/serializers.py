from rest_framework import serializers
from api.models import Task, TaskList
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=200)
    created_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return TaskList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=200)
    created_at = serializers.DateField(required=False)
    due_on = serializers.DateField(required=False)
    status = serializers.CharField(required=False, max_length=200)
    
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')

