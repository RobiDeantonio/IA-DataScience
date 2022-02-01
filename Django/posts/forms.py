""" Posts. forms """

# Django
from django import forms
from django.db.models import fields

# models 
from posts.models import Post

class PostForm(forms.ModelForm):
    """ Post model form """

    class Meta:

        model = Post
        fields = ('user','profile', 'title', 'photo')