from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article

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
