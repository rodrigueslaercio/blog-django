from django import forms 
from ckeditor.fields import RichTextFormField

from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'text': RichTextFormField()
        }
        fields = ["title", "text", "categories", "cover"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Join the discussion and leave a comment!'})
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]