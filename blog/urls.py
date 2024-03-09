"""URLs patterns for blog."""

from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show the page for a single blog post
    path('post/<slug:slug>', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<slug:slug>', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),
    path('author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('category/<int:category_id>', views.category_posts, name='category_posts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)