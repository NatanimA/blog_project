from django.forms import ModelForm
from django import forms
from blog.models import Post,Comments

class PostForm(ModelForm):

    class Meta():
        model= Post
        fields= ['author','title','text']
        widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}), 'text': forms.Textarea(
            attrs={'class': 'editable medium-editor-textarea postcontent'})}


class CommentsForm(ModelForm):

    class Meta():
        model=Comments
        fields=['author','text']
        widgets ={'author':forms.TextInput(attrs={'class': 'textinputclass'}),'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})}
