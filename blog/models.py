from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

User = get_user_model()


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF, Draft"
        PUBLISHED = "PB, Published"

    post_id = models.UUIDField(
        default=uuid4, db_index=True, primary_key=True, editable=False, verbose_name="Blog Post ID",
        help_text="ID of your blog post, automatically generated")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=100, verbose_name="Blog Post Title",
                             help_text="This is the title of your blog post")
    slug = models.SlugField(
        max_length=150, help_text="This is the slug form of the title of your blog post", unique_for_date="publish")
    body = models.TextField(
        help_text="This is the content of your blog post", verbose_name="Blog Post Content")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Blog Post Create Date")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Blog Post Uodate Date")
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(through=UUIDTaggedItem)

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self) -> str:
        return f"{self.post_id}, {self.title}"

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=(self.publish.year, self.publish.month, self.publish.day, self.slug))


class Comment(models.Model):
    comment_id = models.UUIDField(
        default=uuid4, primary_key=True, editable=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=['created'])]

    def __str__(self) -> str:
        return f"Comment by {self.name} on {self.post}"
