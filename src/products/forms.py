from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title",
                  "description",
                  "price"]

class RawProductionForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price =forms.DecimalField()
    
