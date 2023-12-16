from bot.views import (CategoryListView, CreatedByListView, PageDetailView,
                       PostDetailView, PostListView, SearchListView,
                       TagListView)
from django.urls import path

app_name = 'bot'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('created_by/<int:author_pk>/',
         CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
]
