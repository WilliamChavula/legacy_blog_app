from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


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
        max_length=150, help_text="This is the slug form of the title of your blog post", unique_for_date="created")
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

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self) -> str:
        return f"{self.post_id}, {self.title}"
