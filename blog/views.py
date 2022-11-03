from django.shortcuts import render

from blog.service import blog_post_service


def index(request):

    posts = blog_post_service.get_all_posts()
    return render(request, 'blog/index.html', {'posts': posts})
