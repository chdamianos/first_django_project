from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)

app_name = "blog"
urlpatterns = [
    path('<int:id>/', ArticleDetailView.as_view(), name='article'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('', ArticleListView.as_view(), name='article-list'),
]
