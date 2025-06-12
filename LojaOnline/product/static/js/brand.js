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
    console.log("DATA: ", produtos);

    const productsGrid = document.querySelector(".products_grid");
    productsGrid.innerHTML = "";

    const appleGrid = document.getElementById("appleGrid");
    const samsungGrid = document.getElementById("samsungGrid");
    const xiaomiGrid = document.getElementById("xiaomiGrid");

    appleGrid.innerHTML = "";
    samsungGrid.innerHTML = "";
    xiaomiGrid.innerHTML = "";

    produtos.forEach((produto) => {

      if (produto.nome_categoria == "Telefone") {
        // Cria um novo card para cada produto
        const card = document.createElement("div");
        card.classList.add("product_card");

        card.innerHTML = `
                  <div class="product_image apple_image"></div>
                  <h3 class="product_name">${produto.nome}</h3>
                  <div class="product_specs">
                      ${produto.descricao}
                  </div>
                  <div class="product_price apple_price">R$${produto.valor_unitario}</div>
                  <button class="buy_btn apple_btn" onclick="buyProduct('${produto.nome}')">Comprar</button>
              `;

        if (produto.nome_marca == "Apple") {
          appleGrid.appendChild(card);
        }
        if (produto.nome_marca == "Samsung") {
          samsungGrid.appendChild(card);
        }
        if (produto.nome_marca == "Xiaomi") {
          xiaomiGrid.appendChild(card);
        }
      }
    });
  } catch (error) {
    console.error("Erro ao carregar os produtos:", error);
  }
};
