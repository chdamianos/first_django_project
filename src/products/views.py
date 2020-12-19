from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductCreateForm, RawProductionForm
from .models import Product
# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        # confirming delete not actual delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


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


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
