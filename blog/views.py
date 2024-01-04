from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm

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

def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    context = {'form': form}
    return render(request, 'blog/new_post.xhtml', context)