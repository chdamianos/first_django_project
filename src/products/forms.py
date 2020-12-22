from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
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

    class Meta:
        model = Product
        fields = ["title",
                  "description",
                  "price"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # if "CFE" not in title:
        #     raise forms.ValidationError("This is not a valid title")
        # if "new" not in title:
        #     raise forms.ValidationError("This is not a valid title")
        return title


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
