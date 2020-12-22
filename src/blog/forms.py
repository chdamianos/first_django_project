from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    body = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      "placeholder": "Your article",
                                      "class": "new-class-name",
                                      "id": "my-textarea-id",
                                      "rows": 20,
                                      "cols": 120
                                  }))
    author = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Author"
    }))

    class Meta:
        model = Article
        fields = ["title",
                  "body",
                  "author"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        return title