from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

# Create your views here.
def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "blog/article_list.html", context)


def article_detail_view(request, my_id):
    obj = get_object_or_404(Article, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "blog/article_detail.html", context)
