from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'is_active', 'date_joined',)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        depth = 1
        read_only_fields = ['post_id', 'created', 'updated']
        fields = '__all__'
