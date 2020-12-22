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

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'  # <app_name>/<model_name>_list.html
    form_class = ArticleForm
    queryset = Article.objects.all()

    # in case we want to overwrite get_absolute_url in models.py
    # success_url = "/"
    # or
    # def get_sucess_url(self):
    #     return "/"
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'  # <app_name>/<model_name>_list.html
    form_class = ArticleForm
    queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'  # <app_name>/<model_name>_list.html
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all() # we don't need this unless we want to do some processing (e.g. filtering)
    # queryset = Article.objects.filter(id__gt=1) # need to change to 'pk' in urlpatterns in urls.py if we use this. and comment-out the 'get_object'
    # maybe we ca also do filtering in the 'get_object' method

    def get_object(self):
        """
        this is not needed if we use 'pk' instead of 'id' in urlpatterns in urls.py
        """
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
