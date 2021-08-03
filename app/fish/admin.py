from django.contrib import admin
from fish.models import Article, Category, Place, Profile, Comment

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Comment)