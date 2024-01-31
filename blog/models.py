from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Post(models.Model):
    """A blog post made by a user adm"""
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    cover = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        """Returns a string representation of the class"""
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
class Category(models.Model):
    """A category model for the posts"""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """Returns a string representation of the class"""
        return self.name
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author