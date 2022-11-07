from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail_view, name='post_detail'),
]
