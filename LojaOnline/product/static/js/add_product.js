function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

document.getElementById("produtoForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  //Código aqui

  const dados = {
    nome: document.getElementById("nome").value,
    descricao: document.getElementById("descricao").value,
    valor_unitario: parseFloat(document.getElementById("valor_unitario").value),
    quantEstoque_disponivel: parseInt(document.getElementById("quantEstoque_disponivel").value),
    quantEstoque_min: parseInt(document.getElementById("quantEstoque_min").value),
    quantEstoque_max: parseInt(document.getElementById("quantEstoque_max").value),
    id_categoria: parseInt(document.getElementById("id_categoria").value),
    id_fornecedor: document.getElementById("id_fornecedor").value,
  };

  const response = await fetch("/product/add/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify(dados),
  });

  const data = await response.json();

  if (data) {
    alert("Produto adicionado!");
  } else {
    alert(data.erro || "Erro ao adicionar produto");
  }
});

document.getElementById("categoriaForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  let nome = document.getElementById("nome_categoria").value;

  const response = await fetch("/product/category/", {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
    body: JSON.stringify({ nome }),
  });

  const data = await response.json();

  if (data) {
    alert("Categoria adicionado!");
  } else {
    alert(data.erro || "Erro ao adicionar produto");
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

  const response = await fetch("/product/address/", {
    method: "POST",
    headers: { Content_Type: "application/json", "X-CSRFToken": getCSRFToken() },
    body: JSON.stringify(dados),
  });

  const data = await response.json();
  if (data) {
    alert("Fornecedor adicionado!");
  } else {
    alert(data.erro || "Erro ao adicionar produto");
  }
});

document.getElementById("fornecedorForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  const dados = {
    cnpj: document.getElementById("cnpj").value,
    nome_fornecedor: document.getElementById("nome_fornecedor").value,
    email_fornecedor: document.getElementById("email_fornecedor").value,
    telefone_fornecedor: document.getElementById("telefone_fornecedor").value,
    id_endereco: document.getElementById("id_endereco").value,
  };

  const response = await fetch("/product/supplier/", {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
    body: JSON.stringify(dados),
  });

  const data = await response.json();
  if (data) {
    alert("Fornecedor adicionado!");
  } else {
    alert(data.erro || "Erro ao adicionar produto");
  }
});

async function mostrarOpcoes(tipo) {

  const url = `/product/list/${tipo}`;

  try {
    const response = await fetch(url);

    const data = await response.json();

    let titulo = tipo.charAt(0).toUpperCase() + tipo.slice(1);
    let conteudo = `<h3>${titulo}s Cadastrados</h3><ul>`;

    data.resultados.forEach((item) => {
      conteudo += `<li>
                    ${item.nome}
                    <button type="button" onclick="excluirItem('${tipo}', '${item.id}')">Excluir</button>
                    </li>`;
    });

    conteudo += "</ul>";

     const divResultado = document.getElementById("resultados");
        divResultado.innerHTML = conteudo;
        divResultado.style.display = "block";
  } catch (erro) {
    alert("Erro ao buscar " + tipo);
    console.log(erro);
  }
}

async function excluirItem(tipo, id) {
    if (!confirm("Tem certeza que deseja excluir?")) return;

    try {
        const response = await fetch(`/product/excluir/${tipo}/${id}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCSRFToken()
            }
        });

        const data = await response.json();

        if (data) {
            mostrarOpcoes(tipo);  // atualiza a lista
        }
    } catch (erro) {
        alert("Erro ao excluir");
        console.log(erro);
    }
}