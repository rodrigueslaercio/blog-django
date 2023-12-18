from django.shortcuts import render

from .models import Post

def index(request):
    """Home page"""
    posts = Post.objects.order_by('created_at')
    context = {'posts': posts}
    return render(request, 'blog/index.xhtml', context)

def post(request, post_id):
    """Show a single post with full information"""
    post = Post.objects.get(id=post_id)
    categories = post.categories.all()
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/post.xhtml', context)