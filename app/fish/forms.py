from django import forms
from .models import Article, Category, Place, Profile


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fish_category', 'fishing_comment', 'fish_img','length','weight','place']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'icon', 'header', 'text']