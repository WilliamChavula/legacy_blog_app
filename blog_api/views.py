from rest_framework import generics

from .serializers import PostSerializer, Post


class PostsList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    lookup_field = 'post_id'
