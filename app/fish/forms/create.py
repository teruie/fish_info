from django import forms
from django.conf import settings
from fish.models import Article, Category, Place, Profile, Comment

# 投稿
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fish_category', 'fishing_comment', 'fish_img','length','weight','place']

        widgets = {
            'fishing_comment': forms.Textarea(attrs={'class': 'text',}),
        }

# プロフィール
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'icon', 'header', 'text']

# カテゴリー
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass',}),
        }

# 場所
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass',}),
        }