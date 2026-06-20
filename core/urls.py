from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/categories/', views.get_categories, name='get-categories'),
    path('api/search-categories/', views.search_categories, name='search-categories'),
    path('api/hashtags/', views.get_hashtags, name='get-hashtags'),
]