from django.contrib import admin

from .models import Post


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
