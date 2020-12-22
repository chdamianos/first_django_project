from django.urls import path

from .views import (
    article_detail_view,
    article_list_view
)

app_name = "blog"
urlpatterns = [
    path('<int:my_id>/', article_detail_view, name='article'),
    path('', article_list_view, name='article-list'),
]
