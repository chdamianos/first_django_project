from django.urls import path

from .views import (
    article_detail_view,
    ArticleListView
)

app_name = "blog"
urlpatterns = [
    path('<int:my_id>/', article_detail_view, name='article'),
    path('', ArticleListView.as_view(), name='article-list'),
]
