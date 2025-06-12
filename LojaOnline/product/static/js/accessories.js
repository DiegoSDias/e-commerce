  function comprar(produto, preco) {
            alert(`🛒 Produto adicionado ao carrinho!\n\n📱 ${produto}\n💰 R$ ${preco}\n\n✅ Continue comprando ou finalize seu pedido pelo WhatsApp!`);
        }

function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

function buyProduct(productName) {
  // Animação do botão
  event.target.style.transform = "scale(0.95)";
  setTimeout(() => {
    event.target.style.transform = "translateY(-2px)";
  }, 150);
}

window.onload = async () => {
  try {
    const response = await fetch("/product/detalhe/produto/");
    const data = await response.json();

    const produtos = data.resultados;
    console.log("PORDUTOS: ", produtos)
    const productsGrid = document.querySelector(".products_grid");
    productsGrid.innerHTML = "";

    const acessoriosGrid = document.getElementById("acessoriosGrid");
    acessoriosGrid.innerHTML = "";
    produtos.forEach((produto) => {

    if (produto.nome_categoria == "Acessorios") {
        const card = document.createElement("div");
        
        card.classList.add("product_card");
        card.innerHTML = `
                  <div class="product_image apple_image"></div>
                  <h3 class="product_name">${produto.nome}</h3>
                  <div class="product_specs">
                      ${produto.descricao}
                  </div>
                  <div class="product_price">R$${produto.valor_unitario}</div>
                  <button class="buy_btn apple_btn" onclick="buyProduct('${produto.nome}')">Comprar</button>
              `;

        acessoriosGrid.appendChild(card)
    }
    });
  } catch (error) {
    console.error("Erro ao carregar os produtos:", error);
  }
};
