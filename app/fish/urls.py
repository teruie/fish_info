from django.urls import path
from . import views

app_name = 'fish'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #投稿作成
    path('fish/new/', views.ArticleCreateView.as_view(), name='article_create'),
    #投稿詳細
    path('detail/<uuid:pk>/', views.ArticlDetailview.as_view(), name='article_detail'),
    #コメント投稿
    path('detail/<uuid:pk>/comment/', views.CommentCreate.as_view(), name='comment_create'),

    #投稿編集
    path('edit/<uuid:pk>/', views.ArticleUpdateView.as_view(), name='article_edit'),
    #投稿消去
    path('detail/<uuid:pk>/delete/',views.ArticleDeleteview.as_view(),name='article_delete'),

    #なんでも検索
    path('search/', views.SearchView.as_view(), name='search'),
    #魚種検索
    path('category_search/', views.CategorySearchView.as_view(), name='category_search'),
    #魚種検索結果
    path('category_result/', views.CategoryResultView.as_view(), name='category_result'),
    #場所検索
    path('place_search/', views.PlaceSearchView.as_view(), name='place_search'),
    #場所検索結果
    path('place_result/', views.PlaceResultView.as_view(), name='place_result'),
    #みんなの釣果
    path('every_result', views.EveryFishResultView.as_view(), name='every_result'),
    
    #Userページ
    path('mypage/<int:pk>/', views.UserPageDetailView.as_view(), name='mypage_detail'),
    path('mypage/pading/<int:pk>/', views.UserPadingDetailView.as_view(), name='mypage_pading'),
    path('mypage/<int:pk>/edit', views.UserPageUpdateView.as_view(), name='profile_edit'),


    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
