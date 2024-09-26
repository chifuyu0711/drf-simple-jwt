from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentCreateView, MyBlogView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_list_create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/<int:blog_id>/comments/', CommentCreateView.as_view(), name='comment_create'),
    path('my-blogs/', MyBlogView.as_view(), name='my_blog'),
]
