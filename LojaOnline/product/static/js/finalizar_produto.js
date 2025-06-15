function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

// Gerenciamento de endereços
function showenderecoForm() {
  document.getElementById("savedAddress").style.display = "none";
  document.getElementById("enderecoForm").style.display = "block";
}

function cancelNewAddress() {
  document.getElementById("enderecoForm").style.display = "none";
  document.getElementById("savedAddress").style.display = "block";

  // Limpa o formulário
  document
    .getElementById("enderecoForm")
    .querySelectorAll("input, select")
    .forEach((field) => {
      field.value = "";
    });
}

// Formatação automática do CEP
document.getElementById("cep").addEventListener("input", function (e) {
  let value = e.target.value.replace(/\D/g, "");
  if (value.length >= 5) {
    value = value.replace(/^(\d{5})(\d)/, "$1-$2");
  }
  e.target.value = value;
});

// Seleção de forma de pagamento
function selectPayment(type) {
  // Remove seleção anterior
  document.querySelectorAll(".payment-option").forEach((option) => {
    option.classList.remove("selected");
  });

  // Adiciona seleção atual
  event.currentTarget.classList.add("selected");
  document.getElementById(type).checked = true;
}

/*
  // Mostra mensagem de sucesso
  document.getElementById("successMessage").style.display = "block";

  // Scroll suave para a mensagem
  document.getElementById("successMessage").scrollIntoView({
    behavior: "smooth",
  });
*/

// Busca automática de endereço por CEP (simulada)
document.getElementById("cep").addEventListener("blur", function (e) {
  const cep = e.target.value.replace(/\D/g, "");
  if (cep.length === 8) {
    // Aqui você integraria com uma API de CEP real
    // Por agora, apenas simula o preenchimento
  }
});

document.getElementById("enderecoForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  const dados = {
    rua: document.getElementById("rua").value,
    numero: document.getElementById("num_casa").value,
    cep: document.getElementById("cep").value,
    cidade: document.getElementById("cidade").value,
    estado: document.getElementById("estado").value,
    complemento: document.getElementById("complemento").value,
    ponto_referencia: document.getElementById("ponto_referencia").value,
  };

  const editingId = this.dataset.editingId;

  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/endereco/${editingId}/` : "/product/address_user/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
      body: JSON.stringify(dados),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Endereço atualizado!" : "Endereço adicionado!");
      window.location.reload();
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar endereço" : "Erro ao adicionar endereço"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
  }
});

window.onload = async () => {
  const url = `/product/list_user/endereco`;

  try {
    const response = await fetch(url);

    const data = await response.json();

    let conteudo = "";
    if (data.resultados && data.resultados.length > 0) {
      data.resultados.forEach((item) => {
        conteudo += 
                      `
                      <label class="address-option">
                        <input type="radio" name="enderecoSelecionado" value="${item.id}">
                        <strong>${item.nome}</strong>
                        <button type="button" onclick="excluirEndereco('${item.id}')">Excluir</button>
                        <button type="button" onclick="editarItem('endereco', '${item.id}'); showenderecoForm()">Editar</button>
                      </label>
                      <hr>
                    `
      });
    } else {
      conteudo += "<p>Nenhum item encontrado.</p>";
    }

    const divResultado = document.querySelector(".address-details");
    divResultado.innerHTML = conteudo;
  } catch (erro) {
    alert("Erro ao buscar endereço");
    console.error(erro);
  }
};

async function excluirEndereco(id) {
  if (!confirm("Tem certeza que deseja excluir?")) return;

  try {
    const response = await fetch(`/product/excluir_endereco/${id}/`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": getCSRFToken(),
      },
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert("Item excluído com sucesso!");
      window.location.reload();
    } else {
      alert(data.erro || "Erro ao excluir item");
    }
  } catch (erro) {
    alert("Erro ao excluir");
    console.error(erro);
  }
}

async function excluirItem(tipo, id) {
  if (!confirm("Tem certeza que deseja excluir?")) return;

  try {
    const response = await fetch(`/product/excluir/${tipo}/${id}/`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": getCSRFToken(),
      },
    });

    const data = await response.json();
    console.log("Entrou");
    if (response.ok && data.sucesso) {
      alert("Item excluído com sucesso!");
      mostrarOpcoes(tipo); // atualiza a lista
    } else {
      alert(data.erro || "Erro ao excluir item");
    }
  } catch (erro) {
    alert("Erro ao excluir");
    console.error(erro);
  }
}

async function editarItem(tipo, id) {
  const url = `/product/detalhe/${tipo}/${id}/`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    document.getElementById("rua").value = data.rua || "";
    document.getElementById("num_casa").value = data.numero || "";
    document.getElementById("cep").value = data.CEP || "";
    document.getElementById("cidade").value = data.cidade || "";
    document.getElementById("estado").value = data.estado || "";
    document.getElementById("complemento").value = data.complemento || "";
    document.getElementById("ponto_referencia").value = data.ponto_referencia || "";
    document.getElementById("enderecoForm").dataset.editingId = id;
  } catch (error) {
    console.error("Erro ao buscar dados para edição:", error);
    alert("Erro ao carregar dados para edição");
  }
}


async function finalizar_produto() {
  /*
  const endereco_selecionado = document.querySelector("input[name='enderecoSelecionado':checked]");
  if(!endereco_selecionado) {
    alert("Por favor, selecione um endereço de entrega.");
    return;
  }*/

  if (!confirm("Deseja finalizar o pedido?")) return;

  try {
    const response = await fetch("/product/salvar_pedido/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
      body: JSON.stringify() // Não precisa passar o productId aqui
    });

    const data = await response.json();

    if (data) {
      alert("Pedido finalizado com sucesso!");
    } else {
      alert(data.erro || "Erro ao finalizar pedido.");
    }
  } catch (erro) {
    console.error("Erro ao finalizar pedido:", erro);
    alert("Erro de conexão ao finalizar pedido.");
  }
}