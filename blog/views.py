from django.core.paginator import Paginator, Page
from django.shortcuts import render

from blog.service import blog_post_service


def index(request):

    posts = blog_post_service.get_all_posts()

    paginator: Paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    paginated_posts: Page = paginator.page(page_number)

    return render(request, 'blog/index.html', {'posts': paginated_posts})


def post_detail_view(request, year: int, month: int, day: int, slug: str):
    post = blog_post_service.get_post_by_id(year, month, day, slug)

    img_number = request.GET.get('key', 1)
    return render(request, 'blog/post_detail.html', {'post': post, 'img_number': img_number})
