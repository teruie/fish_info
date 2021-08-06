import django.contrib.auth.views
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('logout/', views.logout, name='logout'),
]
