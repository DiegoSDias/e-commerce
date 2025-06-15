function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}


let resultado = []

async function renderizarCarrinho() {
  const container = document.getElementById("cart_items");
  const emptyMessage = document.getElementById("empty_message");
  const summary = document.getElementById("summary");

  const response = await fetch("/product/mostra_carrinho/")
  const data = await response.json()
  resultado = data.resultado

  if (!resultado || resultado.length == 0) {
    container.innerHTML = "";
    emptyMessage.style.display = "block";
    summary.style.display = "none";
    return;
  }

  emptyMessage.style.display = "none";
  summary.style.display = "block";

  container.innerHTML = resultado.map(
      (item) => `
        <div class="cart-item">
            <div class="item-info">
                <div class="item-name">${item.nome}</div>
                <div class="item-price">R$ ${item.valor_unitario}</div>
            </div>
            <div class="quantity-controls">
                <button class="qty-btn" onclick="alterarQuantidade(${item.id_carrinho}, ${item.id_produto}, -1)">-</button>
                <input type="number" class="qty-input" value="${item.quant}" min="1" disabled>
                <button class="qty-btn" onclick="alterarQuantidade(${item.id_carrinho}, ${item.id_produto}, 1)">+</button>
            </div>
            <button class="remove-btn" onclick="removerItem(${item.id_carrinho}, ${item.id_produto})">Remover</button>
        </div>
            `,
    )
    .join("");
    let valor_total = resultado.reduce((total, item) => total + item.valor_unitario * item.quant, 0);

  atualizarResumo(valor_total);
}

async function alterarQuantidade(id_carrinho, id_produto, mudanca) {
  const item = resultado.find((item) => item.id_carrinho === id_carrinho && item.id_produto === id_produto);
  if (item) {
    item.quant += mudanca;
    const dados = {
      id_carrinho: id_carrinho,
      id_produto: id_produto,
      quant: item.quant
    }

    const response = await fetch("/product/editar_quant/", {
      method: "PUT",
      headers: {"Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
      },
      body: JSON.stringify(dados)
    })

    const data = await response.json()

    if (item.quant <= 0) {
      removerItem(id_carrinho, id_produto);
    } else {
      renderizarCarrinho();
    }
  }
}

async function removerItem(id_carrinho, id_produto) {

   const dados = {
      id_carrinho: id_carrinho,
      id_produto: id_produto
   }

   const response = await fetch("/product/remover_item/", {
    method: "DELETE",
    headers: {"X-CSRFToken": getCSRFToken()},
    body: JSON.stringify(dados)
   })
   const data = await response.json()

  renderizarCarrinho();
}

function atualizarResumo(valor) {
  const subtotal = valor
  const frete = 10.0;
  const total = subtotal + frete;

  document.getElementById("subtotal").textContent = `R$ ${subtotal.toFixed(2).replace(".", ",")}`;
  document.getElementById("total").textContent = `R$ ${total.toFixed(2).replace(".", ",")}`;

  if(resultado == []) {
    //document.querySelector(".cart_summary").style.display = "none";
  }
}

renderizarCarrinho();

async function finalizarCompra() {

  window.location.href = "/product/finalizar_produto/"
}