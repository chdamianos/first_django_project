```
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver
python3 manage.py startapp pages
```

# Steps to create new app
1. Run `python3 manage.py startapp <app_name>`
2. Add `<app_name>` to `INSTALLED_APPS` in `settings.py`
3. Add urls in `urls.py` in app folder
    * example
    ```python
    from django.urls import path

    from .views import (
        product_detail_view,
        product_create_view,
        dynamic_lookup_view,
        product_delete_view,
        product_list_view,
        product_update_view
    )

    app_name = "products"
    urlpatterns = [
        path('<int:my_id>/', dynamic_lookup_view, name='product'),
        path('<int:id>/delete/', product_delete_view, name='product-delete'),
        path('<int:id>/update/', product_update_view, name='product-update'),
        path('', product_list_view, name='product-list'),
        path('create/', product_create_view, name='product-list')
    ]
    ```