from django.shortcuts import render

from blog.service import blog_post_service


def index(request):

    posts = blog_post_service.get_all_posts()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail_view(request, year: int, month: int, day: int, slug: str):
    post = blog_post_service.get_post_by_id(year, month, day, slug)

    img_number = request.GET.get('key', 1)
    return render(request, 'blog/post_detail.html', {'post': post, 'img_number': img_number})
