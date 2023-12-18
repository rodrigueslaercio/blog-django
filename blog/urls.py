"""URLs patterns for blog."""

from django.urls import path 
from . import views 

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show the page for a single blog post
    path('post/<int:post_id>', views.post, name='post'),
]