from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from blog.service import blog_post_service
from blog.forms import CommentForm


def index(request):

    posts = blog_post_service.get_all_posts()

    paginator: Paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)

    try:
        paginated_posts: Page = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_posts: Page = paginator.page(1)
    except EmptyPage:
        paginated_posts: Page = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': paginated_posts})


def post_detail_view(request, year: int, month: int, day: int, slug: str):
    post = blog_post_service.get_post_by_slug(year, month, day, slug)

    img_number = request.GET.get('key', 1)
    comments = blog_post_service.get_active_comments_for_post(post=post)
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'img_number': img_number, 'form': form, 'comments': comments})


@require_POST
def post_comment(request, post_id):
    post = blog_post_service.get_post_by_id(post_id)

    comment = None
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        post_url = reverse('blog:post_detail', args=(
            post.publish.year, post.publish.month, post.publish.day, post.slug))
        return redirect(post_url)

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comment': comment})
