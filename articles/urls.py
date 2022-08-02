from django.urls import path
from .views import (
    article_search_view, 
    article_detail_view,
    article_detail_view_slug, 
    article_create_view,
    article_create_view2,
    article_create_view3,
    article_create_view4,
    )

app_name='articles'
urlpatterns = [
    path('', article_search_view, name='search'),
    path('<int:id>/', article_detail_view),
    path('slug/<slug:slug>/', article_detail_view_slug, name='detail'),
    path('create/', article_create_view),
    path('create2/', article_create_view2),
    path('create3/', article_create_view3),
    path('create4/', article_create_view4, name='create'),
]
