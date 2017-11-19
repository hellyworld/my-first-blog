from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):


# Aici modifici structura Posturilor
    class Meta:
        model = Post
        fields = ('title', 'text', 'author')


# Aici modifici structura comentariilor
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
