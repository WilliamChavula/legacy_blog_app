from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('<uuid:post_id>/', views.post_detail_view, name='post_detail'),
]
