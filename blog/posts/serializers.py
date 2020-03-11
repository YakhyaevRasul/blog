from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='posts:post-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'user', 'created_at')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body')


class PostDetailSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
