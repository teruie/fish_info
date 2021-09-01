from django import forms
from django.conf import settings
from fish.models import Article, Category, Place, Profile, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fish_category', 'fishing_comment', 'fish_img','length','weight','place']

        widgets = {
            'fishing_comment': forms.Textarea(attrs={'class': 'text',}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'icon', 'header', 'text']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass',}),
        }


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass',}),
        }