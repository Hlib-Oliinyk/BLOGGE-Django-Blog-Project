from django.db.models import ImageField
from .models import Post
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'topic', 'short_info', 'banner']

        widgets = {
            "title": TextInput(attrs={
                'class': 'post_add_title_text',
                'placeholder': 'Post name'
            }),
            "content": Textarea(attrs={
                'class': 'post_add_content_text',
                'placeholder': 'Post content'
            }),
            "date": DateTimeInput(attrs={
                'class' : 'post_add_date_text',
                'placeholder': 'Post publish date'
            }),
            "topic": TextInput(attrs={
                'class': 'post_add_topic_text',
                'placeholder': 'Post topic'
            }),
            "short_info": TextInput(attrs={
                'class': 'post_add_short_info_text',
                'placeholder': 'Short info about post'
            }),
            "banner": FileInput(attrs={
                'class': 'post_add_banner_text'
            })
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



