from django import forms
from fish.models import Comment



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')