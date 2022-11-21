from django.urls import path
from . import views

app_name = 'blog_api'

urlpatterns = [
    path('posts/', views.PostsList.as_view(), name='post-list'),
    path('posts/<uuid:post_id>', views.PostDetail.as_view(), name='post-detail'),
    path('posts/list_create', views.CreateManyPost.as_view(), name='list_create'),
    path('users/', views.UsersList.as_view(), name='users-list')

]
