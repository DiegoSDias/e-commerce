function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

function showLogin() {
            document.getElementById('loginForm').classList.remove('hidden');
            document.getElementById('signupForm').classList.add('hidden');
        }

function showSignup() {
    document.getElementById('signupForm').classList.remove('hidden');
    document.getElementById('loginForm').classList.add('hidden');
}

function showForgotPassword() {
    alert('Funcionalidade de recuperação de senha ainda não implementada.\nEm um sistema real, isso redirecionaria para a página de recuperação.');
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        const activeForm = document.querySelector('.form:not(.hidden)');
        const submitBtn = activeForm.querySelector('.btn');
        submitBtn.click();
    }
});

window.onload = () => {

    const formLogin = document.getElementById("login_form");
    console.log(formLogin)
    if (formLogin) {
        let teste = false;
        formLogin.addEventListener("submit", async function (event) {
            event.preventDefault();
            if(teste) return 
            teste = true;
            
            const dados = {
                email: document.getElementById("emailLogin").value,
                senha: document.getElementById("senhaLogin").value
            }

            const response = await fetch("/login_register/login/", {
            method: "POST",
            headers: {"Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify(dados)
            })

            const data = await response.json()
            
            if(data){
                window.location.href = menu
            }
            else {
                alert("Erro ao fazer login")
            }
        submitted = false;
        })
    }
    
    const form = document.getElementById("cadastro_form");
    if (form) {
        let submitted = false;
        form.addEventListener("submit", async function (event) {
            event.preventDefault(); 

        if (submitted) return;
        submitted = true;

            const dados = {
                nome: document.getElementById("nome").value,
                cpf: document.getElementById("cpf").value,
                email: document.getElementById("email").value,
                telefone: document.getElementById("telefone").value,
                data_nascimento: document.getElementById("data_nascimento").value,
                senha: document.getElementById("senha").value,
            };
            let confirmar_senha = document.getElementById("confirmar_senha").value;

            if (dados.senha !== confirmar_senha) {
                alert("As senhas não coincidem!");
                return;
            }

            const response = await fetch("/login_register/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify(dados)
            });

            const data = await response.json();

            if (data.sucesso) {
                window.location.href = welcome
            } else {
                alert(data.erro || "Erro ao cadastrar.");
            }
        });
    submitted = false;
    }
    
};

