from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def all_tags():
    return Post.tags.all()
