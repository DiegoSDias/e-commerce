document.addEventListener("DOMContentLoaded", function () {

  const searchInput = document.querySelector(".search_bar input");
  const searchBtn = document.querySelector(".search_btn");

  searchBtn.addEventListener("click", function () {
    const searchContent = searchInput.value.trim();
    if (searchContent) {
      alert(`Buscando por: ${searchContent}`);
      // Aqui você implementaria a lógica de busca real
    }
  });

  searchInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      searchBtn.click();
    }
  });

  /*
  const options_menu = document.querySelectorAll(".option_menu a");
  options_menu.forEach((option) => {
    option.addEventListener("click", function (e) {
      e.preventDefault();
      const option_chosen = this.textContent.trim();
      if (!this.parentElement.querySelector(".dropdown")) {
        alert(`Navegando para: ${option_chosen}`);
      }
    });
  });
  */
});