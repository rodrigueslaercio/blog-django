from django import forms 

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "categories", "cover"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Join the discussion and leave a comment!'})
        }