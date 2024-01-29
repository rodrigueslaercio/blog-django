"""URLs patterns for blog."""

from django.urls import path 
from . import views 

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show the page for a single blog post
    path('post/<slug:slug>', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<slug:slug>', views.edit_post, name='edit_post'),
    path('author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('category/<int:category_id>', views.category_posts, name='category_posts'),
]