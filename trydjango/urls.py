"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import simple_response, using_model, using_format, using_template1, using_template2, list_data1, list_data2
from articles.views import (
    article_search_view, 
    article_detail_view,
    article_detail_view_slug, 
    article_create_view,
    article_create_view2,
    article_create_view3,
    article_create_view4,
    )
from accounts.views import (
    login_view_old,
    login_view,
    logout_view,
    register_view,
    )

from search.views import search_view

urlpatterns = [
    #base work:
    path('', list_data2), #usefull to have this home page
    path('library/recipes/', include('recipes.urls')), #allow to connect url from app to general url + way to reverse url
    path('library/articles/', include('articles.urls')),
    path('simple_response/', simple_response),
    path('using_model/', using_model),
    path('using_format/', using_format),
    path('using_template1/', using_template1),
    path('using_template2/', using_template2),
    path('list_data1/', list_data1),
    path('list_data2/', list_data2),
    #work on specific app articles:
    # path('articles/', article_search_view),
    # path('articles/<int:id>/', article_detail_view),
    # path('articles/slug/<slug:slug>/', article_detail_view_slug, name='article-detail'),
    # path('articles/create/', article_create_view),
    # path('articles/create2/', article_create_view2),
    # path('articles/create3/', article_create_view3),
    # path('articles/create4/', article_create_view4, name='article-create'),
    #login mechanism:
    path('search/', search_view, name='search'),
    path('login_old/', login_view_old),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('admin/', admin.site.urls),
]
