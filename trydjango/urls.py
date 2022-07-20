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
from django.urls import path
from .views import simple_response, using_model, using_format, using_template1, using_template2, list_data1, list_data2
from articles.views import (
    article_search_view, 
    article_detail_view, 
    article_create_view
    )
from accounts.views import (
    login_view,
    logout_view,
    )

urlpatterns = [
    #base work:
    path('', list_data2), #usefull to have this home page
    path('simple_response/', simple_response),
    path('using_model/', using_model),
    path('using_format/', using_format),
    path('using_template1/', using_template1),
    path('using_template2/', using_template2),
    path('list_data1/', list_data1),
    path('list_data2/', list_data2),
    #work on specific app articles:
    path('articles/', article_search_view),
    path('articles/<int:id>/', article_detail_view),
    path('articles/create/', article_create_view),
    #login mechanism:
    path('login/', login_view),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
]
