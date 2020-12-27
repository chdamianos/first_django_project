```
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver
python3 manage.py startapp pages
```

# Steps to create new app
1. Run `python3 manage.py startapp <app_name>`
2. Add `<app_name>` to `INSTALLED_APPS` in `settings.py`
3. Create views in `<app_name>/views.py`
4. Import views and add urls in `urls.py` in app folder
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
5. Add urls in project level `urls.py`
    * example
    ```python
    from django.contrib import admin
    from django.urls import path, include

    from pages.views import homepage_view, contacts_view, about_view

    urlpatterns = [
        path("products/", include("products.urls")),
        path('', homepage_view, name="home"),
        path('contact/', contacts_view),
        path('about/', about_view),
        path('admin/', admin.site.urls)
    ]
    ```
6. Add templates in `<app_name>/templates/<app_name>/file.html`
7. Add models in `<app_name>/models.py`
8. Register models in `<app_name>/admin.py`
    * example
    ```python
    from .models import Product
    admin.site.register(Product)
    ```
9. Update database from shell
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```