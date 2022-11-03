from blog.models import Post


def get_all_posts():
    """
    Retrieves all published posts from the Database.

    :return: Queryset<Post> object
    """
    return Post.published.all()
