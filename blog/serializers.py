from rest_framework import serializers
from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'author', 'created_at', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'body', 'created_at']
