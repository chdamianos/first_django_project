from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={"id": self.id})#alternatively  reverse("blog:article-list")
