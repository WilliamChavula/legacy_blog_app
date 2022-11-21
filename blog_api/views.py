from rest_framework import generics

from .serializers import PostSerializer, Post, UserSerializer, User


class PostsList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    lookup_field = 'post_id'


class CreateManyPost(generics.CreateAPIView):
    serializer_class = PostSerializer

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, many=True, **kwargs)


class UsersList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
