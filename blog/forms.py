from django import forms

from .models import Post


class PostForm(forms.ModelForm):


# De aici modifici cotinutul afisat in PostForm clasa Meta!
    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'created_date', 'published_date')