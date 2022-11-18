from django import forms

from .models import PostModel


class NewPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'text', 'author', 'status']

        