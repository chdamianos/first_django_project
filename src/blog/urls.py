from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = "blog"
urlpatterns = [
    path('<int:id>/', ArticleDetailView.as_view(), name='article'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('', ArticleListView.as_view(), name='article-list'),
]
