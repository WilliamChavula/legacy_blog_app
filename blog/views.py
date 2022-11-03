from django.shortcuts import render
from blog.models import Post

from blog.service import blog_post_service


def index(request):

    posts = blog_post_service.get_all_posts()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail_view(request, post_id: str):
    post = blog_post_service.get_post_by_id(post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
