from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post, Category, Comment
from .forms import PostForm, CommentForm, CategoryForm

def index(request):
    """Home page"""
    search_post = request.GET.get('search')
    
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post))
    else:
        posts = Post.objects.order_by('-created_at')
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'blog/index.xhtml', context)

def post(request, slug):
    """Show a single post with full information"""
    post = get_object_or_404(Post, slug=slug)
    
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user 
            form.post = post 
            form.save()
            return redirect('blog:post', slug=post.slug)
    comments = Comment.objects.filter(post=post)
    categories = post.categories.all()
    # gets the 4 most recents posts
    recent_posts = Post.objects.order_by('-created_at')[:4]
    context = {'post': post, 'categories': categories, 'comments':comments, 'form': form, 'recent_posts':recent_posts}
    return render(request, 'blog/post.xhtml', context)
    

@login_required
def new_post(request):
    if not request.user.is_staff:
       return redirect('blog:index')
    
    """Add a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST, files=request.FILES) 
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            # handle many to many relationship // fix the categories issue
            form.save_m2m()
            return redirect('blog:index')
    context = {'form': form}
    return render(request, 'blog/new_post.xhtml', context)

@login_required
def edit_post(request, slug):
    if not request.user.is_staff:
       return redirect('blog:index')
    
    """Edit an existing post"""
    post = get_object_or_404(Post, slug=slug)
    
    if request.method != 'POST':
        # Initial request, fill the form with the current content
        form = PostForm(instance=post)
    else:
        # POST data submitted, process it 
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:post', slug=post.slug)
    context = {'post':post, 'form':form}
    return render(request, 'blog/edit_post.xhtml', context)

@login_required
def delete_post(request, slug):
    if not request.user.is_staff:
        return redirect('blog:index')
    
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog:index')

def author_posts(request, author_id):
    """Shows all the posts made by an author"""
    posts = Post.objects.filter(author_id = author_id).order_by('-created_at')
    author = posts.first().author.username
    context = {'posts': posts, 'author': author}
    return render(request, 'blog/author_posts.xhtml', context)

def category_posts(request, category_id):
    """Shows all the posts within the category"""
    category = Category.objects.get(id = category_id)
    posts = Post.objects.filter(categories = category)
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    context = {'posts':posts, 'page_obj': page_obj, 'category': category}
    return render(request, 'blog/category.xhtml', context)

def categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return context

@login_required
def new_category(request):
    if not request.user.is_staff:
        return redirect('blog:index')
    
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    context = {'form' : form}
    return render(request, 'blog/new_category.xhtml', context)
        