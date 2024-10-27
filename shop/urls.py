from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import article_list, article_detail

urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:article_id>/', article_detail, name='article_detail'),
]