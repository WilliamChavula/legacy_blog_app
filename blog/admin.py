from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "publish",
        "created",)
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'updated', 'active',)
    list_filter = ('active', 'created', 'updated',)
    search_fields = ('name', 'email', 'body',)
