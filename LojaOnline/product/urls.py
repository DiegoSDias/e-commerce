from django.urls import path
from .views import smartphones, brand, accessories, promotion, launch, cart, smartphones_marca, adicionar_produto, add_product, add_category, add_supplier, add_address, listar_opcoes, excluir_item

urlpatterns = [
    path("smartphones/", smartphones, name="smartphones"),
    path("smartphones/<str:marca>", smartphones_marca, name="smartphones_marca"),
    path("smartphones/<str:categoria>", smartphones_marca, name="smartphones_categoria"),
    path("smartphones/<str:acessorio>", smartphones_marca, name="smartphones_acessorio"),
    path("brand/", brand, name="brand"),
    path("accessories/", accessories, name="accessories"),
    path("promotion/", promotion, name="promotion"),
    path("launch/", launch, name="launch"),
    path("cart/", cart, name="cart"),
    path('add_product/', adicionar_produto, name="add_product"),
    path('add/', add_product, name="add"),
    path("category/", add_category, name="category"),
    path("supplier/", add_supplier, name="supplier"),
    path("address/", add_address, name="address"),
    path("list/<str:tipo>/", listar_opcoes, name="list_options"),
    path("excluir/<str:tipo>/<str:id>/", excluir_item, name="excluir"),
]
