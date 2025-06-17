function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

function showForm(formType) {
  // Ocultar todos os containers
  const containers = ["produto", "categoria", "marca", "endereco", "fornecedor"];
  containers.forEach((container) => {
    const element = document.getElementById("container-" + container);
    if (element) {
      element.style.display = "none";
    }
  });

  // Remover classe active de todos os botões
  const tabs = document.querySelectorAll(".nav-tab");
  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });

  // Mostrar o container selecionado
  const selectedContainer = document.getElementById("container-" + formType);
  if (selectedContainer) {
    selectedContainer.style.display = "block";
  }

  // Adicionar classe active ao botão clicado
  event.target.classList.add("active");
}

document.getElementById("produtoForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  const dados = {
    nome: document.getElementById("nome").value,
    descricao: document.getElementById("descricao").value,
    valor_unitario: parseFloat(document.getElementById("valor_unitario").value),
    quantEstoque_disponivel: parseInt(document.getElementById("quantEstoque_disponivel").value),
    quantEstoque_min: parseInt(document.getElementById("quantEstoque_min").value),
    quantEstoque_max: parseInt(document.getElementById("quantEstoque_max").value),
    id_categoria: parseInt(document.getElementById("id_categoria").value),
    id_fornecedor: document.getElementById("id_fornecedor").value,
    id_marca: parseInt(document.getElementById("id_marca").value),
  };

  if (!validarDados(dados, "produto")) return;

  const editingId = this.dataset.editingId;
  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/produto/${editingId}/` : "/product/add/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
      body: JSON.stringify(dados),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Produto atualizado!" : "Produto adicionado!");
      if (editingId) {
        cancelarEdicao("produto");
      } else {
        this.reset();
      }
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar produto" : "Erro ao adicionar produto"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
  }
});

document.getElementById("categoriaForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  let nome = document.getElementById("nome_categoria").value;

  const editingId = this.dataset.editingId;
  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/categoria/${editingId}/` : "/product/category/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
      body: JSON.stringify({ nome }),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Categoria atualizada!" : "Categoria adicionada!");
      if (editingId) {
        cancelarEdicao("categoria");
      } else {
        this.reset();
      }
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar categoria" : "Erro ao adicionar categoria"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
  }
});

document.getElementById("marcaForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  let nome = document.getElementById("nome_marca").value;

  const editingId = this.dataset.editingId;
  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/marca/${editingId}/` : "/product/marca/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
      body: JSON.stringify({ nome }),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Marca atualizada!" : "Marca adicionada!");
      if (editingId) {
        cancelarEdicao("marca");
      } else {
        this.reset();
      }
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar marca" : "Erro ao adicionar marca"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
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

  if (!validarDados(dados, "endereco")) return;

  const editingId = this.dataset.editingId;
  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/endereco/${editingId}/` : "/product/address/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
      body: JSON.stringify(dados),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Endereço atualizado!" : "Endereço adicionado!");
      if (editingId) {
        cancelarEdicao("endereco");
      } else {
        this.reset();
      }
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar endereço" : "Erro ao adicionar endereço"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
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

  if (!validarDados(dados, "fornecedor")) return;

  const editingId = this.dataset.editingId;
  const method = editingId ? "PUT" : "POST";
  const url = editingId ? `/product/edit/fornecedor/${editingId}/` : "/product/supplier/";

  try {
    const response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
      body: JSON.stringify(dados),
    });

    const data = await response.json();

    if (response.ok && data.sucesso) {
      alert(editingId ? "Fornecedor atualizado!" : "Fornecedor adicionado!");
      if (editingId) {
        cancelarEdicao("fornecedor");
      } else {
        this.reset();
      }
    } else {
      alert(data.erro || (editingId ? "Erro ao atualizar fornecedor" : "Erro ao adicionar fornecedor"));
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão");
  }
});

async function mostrarOpcoes(tipo) {
  const url = `/product/list/${tipo}`;

  try {
    const response = await fetch(url);

    const data = await response.json();

    let titulo = tipo.charAt(0).toUpperCase() + tipo.slice(1);
    let conteudo = `<h3>${titulo}s Cadastrados</h3>`;

    if (data.resultados && data.resultados.length > 0) {
      conteudo += "<ul>";
      data.resultados.forEach((item) => {
        conteudo += `<li>
                      ${item.nome}
                      <button type="button" onclick="excluirItem('${tipo}', '${item.id}')">Excluir</button>
                      <button type="button" onclick="editarItem('${tipo}', '${item.id}')">Editar</button>
                      </li>`;
      });
      conteudo += "</ul>";
    } else {
      conteudo += "<p>Nenhum item encontrado.</p>";
    }

    const divResultado = document.getElementById("resultados");
    divResultado.innerHTML = conteudo;
    divResultado.style.display = "block";
  } catch (erro) {
    alert("Erro ao buscar " + tipo);
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

    if (tipo === "produto") {
      document.getElementById("nome").value = data.nome || "";
      document.getElementById("descricao").value = data.descricao || "";
      document.getElementById("valor_unitario").value = data.valor_unitario || "";
      document.getElementById("quantEstoque_disponivel").value = data.quantEstoque_disponivel || "";
      document.getElementById("quantEstoque_min").value = data.quantEstoque_min || "";
      document.getElementById("quantEstoque_max").value = data.quantEstoque_max || "";
      document.getElementById("id_categoria").value = data.id_categoria || "";
      document.getElementById("id_fornecedor").value = data.id_fornecedor || "";

      document.getElementById("produtoForm").dataset.editingId = id;
      atualizarInterface("produto", true);
    }

    if (tipo == "categoria") {
      document.getElementById("nome_categoria").value = data.nome || "";
      document.getElementById("categoriaForm").dataset.editingId = id;
      atualizarInterface("categoria", true);
    }

    if (tipo == "marca") {
      document.getElementById("nome_marca").value = data.nome || "";
      document.getElementById("marcaForm").dataset.editingId = id;
      atualizarInterface("marca", true);
    }

    if (tipo == "fornecedor") {
      document.getElementById("cnpj").value = data.CNPJ || data.cnpj || "";
      document.getElementById("nome_fornecedor").value = data.nome || "";
      document.getElementById("email_fornecedor").value = data.email || "";
      document.getElementById("telefone_fornecedor").value = data.telefone || "";
      document.getElementById("id_endereco").value = data.id_endereco || "";
      document.getElementById("fornecedorForm").dataset.editingId = id;
      atualizarInterface("fornecedor", true);
    }

    if (tipo == "endereco") {
      document.getElementById("rua").value = data.rua || "";
      document.getElementById("num_casa").value = data.numero || "";
      document.getElementById("cep").value = data.CEP || "";
      document.getElementById("cidade").value = data.cidade || "";
      document.getElementById("estado").value = data.estado || "";
      document.getElementById("complemento").value = data.complemento || "";
      document.getElementById("ponto_referencia").value = data.ponto_referencia || "";
      document.getElementById("enderecoForm").dataset.editingId = id;
      atualizarInterface("endereco", true);
    }
  } catch (error) {
    console.error("Erro ao buscar dados para edição:", error);
    alert("Erro ao carregar dados para edição");
  }
}

// Função para atualizar títulos e botões baseado no modo de edição
function atualizarInterface(tipo, editando = false) {
  const titulo = document.getElementById(`${tipo}Title`);
  const botao = document.getElementById(`${tipo}SubmitBtn`);

  if (editando) {
    titulo.textContent = `Editar ${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`;
    botao.textContent = `Atualizar ${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`;
  } else {
    titulo.textContent = `Adicionar ${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`;
    botao.textContent = `Salvar ${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`;
  }
}

// Função para cancelar edição
function cancelarEdicao(tipo) {
  const form = document.getElementById(`${tipo}Form`);
  delete form.dataset.editingId;
  form.reset();
  atualizarInterface(tipo, false);
}

// Função para validar dados antes do envio
function validarDados(dados, tipo) {
  if (tipo === "produto") {
    if (dados.valor_unitario <= 0) {
      alert("O valor unitário deve ser maior que zero");
      return false;
    }
    if (dados.quantEstoque_min > dados.quantEstoque_max) {
      alert("O estoque mínimo não pode ser maior que o estoque máximo");
      return false;
    }
  }

  if (tipo === "fornecedor") {
    // Validação básica de CNPJ (apenas números e tamanho)
    const cnpj = dados.cnpj.replace(/\D/g, "");
    if (cnpj.length !== 14) {
      alert("CNPJ deve ter 14 dígitos");
      return false;
    }
  }

  if (tipo === "endereco") {
    // Validação básica de CEP
    const cep = dados.cep.replace(/\D/g, "");
    if (cep.length !== 8) {
      alert("CEP deve ter 8 dígitos");
      return false;
    }
  }

  return true;
}
