from django.urls import path
from . import views

app_name = 'fish'

urlpatterns = [
    path('', views.index, name='index'),

    #投稿作成
    path('fish/new/', views.article_create, name='article_create'),
    #投稿詳細
    path('detail/<uuid:pk>/', views.article_detail, name='article_detail'),
    #コメント投稿
    path('detail/<uuid:pk>/comment/', views.comment_create, name='comment_create'),

    #投稿編集
    path('edit/<uuid:pk>/', views.article_edit, name='article_edit'),
    #投稿消去
    path('detail/<uuid:pk>/delete/',views.article_delete,name='article_delete'),

    #なんでも検索
    path('search/', views.search, name='search'),
    #魚種検索
    path('category_search/', views.category_search, name='category_search'),
    #魚種検索結果
    path('category_result/', views.category_result, name='category_result'),
    #場所検索
    path('place_search/', views.place_search, name='place_search'),
    #場所検索結果
    path('place_result/', views.place_result, name='place_result'),

    #みんなの釣果
    path('every_result', views.every_result, name='every_result'),
    
    #Userページ
    path('mypage/<int:pk>/', views.mypage_detail, name='mypage_detail'),
    path('mypage/pading/<int:pk>/', views.mypage_pading, name='mypage_pading'),
    path('mypage/<int:pk>/edit', views.profile_edit, name='profile_edit'),


    path('contact/', views.contact_form, name='contact_form'),
    path('contact/result/', views.contact_result, name='contact_result'),
]
