from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title",
                  "description",
                  "price"]


class RawProductionForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      "placeholder": "Your description",
                                      "class": "new-class-name",
                                      "id": "my-textarea-id",
                                      "rows": 20,
                                      "cols": 120
                                  }))
    price = forms.DecimalField(initial=199.99)
