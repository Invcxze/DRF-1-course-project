from django.urls import path

from shop import views

urlpatterns = [
    path('products', views.get_list_of_products),
    path('product', views.create_product),
    path('product/<int:pk>', views.update_or_delete_product),
    path('cart', views.get_list_of_products_from_cart),
    path('cart/<int:pk>', views.add_or_delete_product_from_cart),
    path('order', views.get_list_of_products_from_order),
]
