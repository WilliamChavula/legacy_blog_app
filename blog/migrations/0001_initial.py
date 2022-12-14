# Generated by Django 4.1.3 on 2022-11-01 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='ID of your blog post, automatically generated', primary_key=True, serialize=False, verbose_name='Blog Post ID')),
                ('title', models.CharField(help_text='This is the title of your blog post', max_length=100, verbose_name='Blog Post Title')),
                ('slug', models.SlugField(help_text='This is the slug form of the title of your blog post', max_length=150, unique_for_date='created')),
                ('body', models.TextField(help_text='This is the content of your blog post', verbose_name='Blog Post Content')),
                ('status', models.CharField(choices=[('DF, Draft', 'Draft'), ('PB, Published', 'Published')], default='DF, Draft', max_length=20)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Blog Post Create Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Blog Post Uodate Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx'),
        ),
    ]
