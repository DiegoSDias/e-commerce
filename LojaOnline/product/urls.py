from django.urls import path
from .views import smartphones, brand, accessories, cart, adicionar_produto, add_product, add_category, add_marca, add_supplier, add_address, listar_opcoes, excluir_item, detalhe_produto, detalhe_item, edit_item

urlpatterns = [
    path("smartphones/", smartphones, name="smartphones"),
    path("brand/", brand, name="brand"),
    path("accessories/", accessories, name="accessories"),
    path("cart/", cart, name="cart"),
    path('add_product/', adicionar_produto, name="add_product"),
    path('add/', add_product, name="add"),
    path("category/", add_category, name="category"),
    path("marca/", add_marca, name="marca"),
    path("supplier/", add_supplier, name="supplier"),
    path("address/", add_address, name="address"),
    path("list/<str:tipo>/", listar_opcoes, name="list_options"),
    path("excluir/<str:tipo>/<str:id>/", excluir_item, name="excluir"),
    path("detalhe/<str:tipo>/", detalhe_produto, name="detalhe_produto"),
    path('detalhe/<str:tipo>/<str:id>/', detalhe_item, name='detalhe_item'),
    path("edit/<str:tipo>/<str:id>/", edit_item, name="edit_item"),
]
