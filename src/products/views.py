from django.shortcuts import render
from .forms import ProductCreateForm, RawProductionForm
from .models import Product
# Create your views here.


def render_initial_data(request):
    initial_data = {
        "title": "This is my awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductCreateForm(request.POST or None,
                             initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = RawProductionForm()
#     if request.method == 'POST':
#         form = RawProductionForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     print(request.POST.get('title'))
#     context = {}
#     return render(request, "products/product_create.html", context)
# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
