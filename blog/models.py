from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    """A blog post made by a user adm"""
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("Category", related_name="posts", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        """Returns a string representation of the class"""
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
class Category(models.Model):
    """A category model for the posts"""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """Returns a string representation of the class"""
        return self.name