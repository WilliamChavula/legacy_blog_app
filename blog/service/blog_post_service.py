from django.shortcuts import get_object_or_404

from blog.models import Post


def get_all_posts():
    """
    Retrieves all published posts from the Database.

    :return: Queryset<Post> object
    """

    return Post.published.all()


def get_post_by_slug(year: int, month: int, day: int, slug: str):
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day,
                             status=Post.Status.PUBLISHED)

    return post


def get_post_by_id(post_id: str):
    post = get_object_or_404(Post, post_id=post_id,
                             status=Post.Status.PUBLISHED)

    return post


def get_active_comments_for_post(post: Post):
    comments = post.comments.filter(active=True)

    return comments
