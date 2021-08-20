from django import forms
from django.conf import settings
from fish.models import Article, Category, Place, Profile, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fish_category', 'fishing_comment', 'fish_img','length','weight','place']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'icon', 'header', 'text']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title']


