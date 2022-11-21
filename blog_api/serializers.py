from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'email': instance.email,
            'is_active': instance.is_active,
            'date_joined': instance.date_joined
        }


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True)

    class Meta:
        model = Post
        read_only_fields = ('post_id', 'created', 'updated',)
        fields = '__all__'

    # def create(self, validated_data):
    #     author = validated_data.pop('author')
    #
    #     try:
    #         author_in_db = User.objects.get(username=author['username'])
    #
    #         # return Post.objects.create(**validated_data, author=author_in_db)
    #         new_post = Post(**validated_data, author=author_in_db)
    #         new_post.save()
    #
    #         return new_post
    #
    #     except User.DoesNotExist:
    #         new_author = User(**author)
    #         new_author.set_password(author['password'])
    #         new_author.save()
    #
    #         new_post = Post(**validated_data, author=new_author)
    #         new_post.save()
    #
    #         return new_post
