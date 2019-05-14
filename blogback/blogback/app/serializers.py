from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        
class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=200)
    body = serializers.CharField(required=False, max_length=200)
    like_count = serializers.IntegerField(required=False)
    created_at = serializers.DateField(required=False)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'like_count','created_at' ,'created_by')

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.like_count = validated_data.get(
            'like_count ', instance.like_count)
        instance.save()
        return instance


