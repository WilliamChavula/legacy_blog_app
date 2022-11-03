from django.shortcuts import get_object_or_404

from blog.models import Post


def get_all_posts():
    """
    Retrieves all published posts from the Database.

    :return: Queryset<Post> object
    """
    return Post.published.all()


def get_post_by_id(post_id: str):
    post = get_object_or_404(Post, post_id=post_id,
                             status=Post.Status.PUBLISHED)

    return post
