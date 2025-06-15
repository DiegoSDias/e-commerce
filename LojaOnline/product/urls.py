from django.urls import path
from .views import (smartphones, brand, accessories, cart, adicionar_produto, add_product, 
                    add_category, add_marca, add_supplier, add_address,add_address_user, 
                    listar_opcoes, listar_end_usuario, excluir_item, excluir_endereco, 
                    detalhe_produto, detalhe_item, edit_item, finalizar_produto, salvar_pedido, 
                    criar_carrinho, mostra_carrinho, editar_quant, remover_item)

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
    path("address_user/", add_address_user, name="address_user"),
    path("list/<str:tipo>/", listar_opcoes, name="list_options"),
    path("list_user/<str:tipo>/", listar_end_usuario, name="list_end_user"),
    path("excluir/<str:tipo>/<str:id>/", excluir_item, name="excluir"),
    path("excluir_endereco/<str:id>/", excluir_endereco, name="excluir_endereco"),
    path("detalhe/<str:tipo>/", detalhe_produto, name="detalhe_produto"),
    path('detalhe/<str:tipo>/<str:id>/', detalhe_item, name='detalhe_item'),
    path("edit/<str:tipo>/<str:id>/", edit_item, name="edit_item"),
    path("finalizar_produto/", finalizar_produto, name="finalizar_produto"),
    path("salvar_pedido/", salvar_pedido, name="salvar_pedido"),
    path("add_cart/", criar_carrinho, name="criar_carrinho"),
    path("mostra_carrinho/", mostra_carrinho, name="mostra_carrinho"),
    path("editar_quant/", editar_quant, name="editar_quant"),
    path("remover_item/", remover_item, name="remover_item"),


]
