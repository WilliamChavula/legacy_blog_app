from django import forms
from django.forms import ModelForm

from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control',  'rows': "5", 'placeholder': "Enter Your Comment Here"}),
        }
        help_texts = {
            'name': 'Enter your name',
            'email': 'Enter your email',
            'body': 'Enter your comment',
        }
