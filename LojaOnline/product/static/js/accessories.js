function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
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

    if (produto.nome_categoria.toUpperCase() != "TELEFONE" &&
        produto.nome_categoria.toUpperCase() != "TELEFONES" &&
        produto.nome_categoria.toUpperCase() != "CELULAR" &&
        produto.nome_categoria.toUpperCase() != "CELULARES"
  ) {
        const card = document.createElement("div");
        
        card.classList.add("product_card");
        card.innerHTML = `
                  <div class="product_image apple_image"></div>
                  <h3 class="product_name">${produto.nome}</h3>
                  <div class="product_specs">
                      ${produto.descricao}
                  </div>
                  <div class="product_price">R$${produto.valor_unitario}</div>
                   <button class="buy_btn apple_btn" onclick="viewProduct('${produto.id_produto}', '${produto.nome}', '${produto.descricao}', '${produto.valor_unitario}')">Ver Produto</button>
              `;

        acessoriosGrid.appendChild(card)
    }
    });
  } catch (error) {
    console.error("Erro ao carregar os produtos:", error);
  }
};

function viewProduct(id, nome, descricao, preco) {
  currentProduct = { nome, descricao, preco };

  document.getElementById("modalName").textContent = nome;
  document.getElementById("modalDescription").textContent = descricao;
  document.getElementById("modalPrice").textContent = `R$ ${preco}`;

  document.getElementById("modalProductId").value = id;
  document.getElementById("productModal").style.display = "block";
}

function closeModal() {
  document.getElementById("productModal").style.display = "none";
  currentProduct = null;
}

function buyProduct() {
  if (currentProduct) {
   
    alert(`Comprando: ${currentProduct.nome} por R$ ${currentProduct.preco}`);
    closeModal();
  }
}

async function addToCart() {
  if (currentProduct) {
    const productId = document.getElementById("modalProductId").value;

    const response = await fetch(`/product/add_cart/`, {
      method: "POST",
      headers: {'Content-Type':'application/json', 
        "X-CSRFToken": getCSRFToken()
      },
      body: JSON.stringify({productId})
    })

    alert(`Adicionado ao carrinho: ${currentProduct.nome}`);
    closeModal();
  }
}

window.onclick = function (event) {
  const modal = document.getElementById("productModal");
  if (event.target == modal) {
    closeModal();
  }
};
