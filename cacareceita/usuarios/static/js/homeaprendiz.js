document.addEventListener('DOMContentLoaded', function () {
    const apiKey = '030af2ba4b0b4a36b82f165e979d4f44'; // Substitua pela sua chave de API da Spoonacular
    const recipesContainer = document.querySelector('.conteudo-receitas');

    function searchRecipes() {
        recipesContainer.innerHTML = ''; // Limpa o conteúdo atual

        // Busca um total de 23 receitas
        fetch(`https://api.spoonacular.com/recipes/complexSearch?number=23&apiKey=${apiKey}`)
            .then(response => response.json())
            .then(data => {
                let row; // Variável para manter a referência da linha atual

                // Itera sobre as receitas e cria os cards
                data.results.forEach((recipe, index) => {
                    // A cada 4 receitas ou na primeira receita, cria uma nova linha
                    if (index % 4 === 0 || index === 0) {
                        row = document.createElement('div');
                        row.classList.add('linha-cardReceita'); // Adicione sua classe para estilização das linhas aqui
                        recipesContainer.appendChild(row);
                    }

                    // Cria o card da receita
                    const cardReceitaLink = document.createElement('a');
                    cardReceitaLink.href = `javascript:void(0);`; // Evita redirecionamento
                    cardReceitaLink.className = 'cardReceita';
                    cardReceitaLink.dataset.recipeId = recipe.id; // Armazena o ID da receita no elemento

                    // Adiciona a imagem da receita
                    const imagemReceita = document.createElement('img');
                    imagemReceita.className = 'foto-receita';
                    imagemReceita.src = recipe.image;
                    cardReceitaLink.appendChild(imagemReceita);

                    // Adiciona o título da receita
                    const tituloReceita = document.createElement('p');
                    tituloReceita.textContent = recipe.title;
                    cardReceitaLink.appendChild(tituloReceita);

                    // Adiciona evento de clique para armazenar o ID da receita e redirecionar
cardReceitaLink.addEventListener('click', function() {
    localStorage.setItem('receitaId', this.dataset.recipeId); // Armazena o ID no localStorage
    const receitaAprendizUrl = document.getElementById('recipeUrl').dataset.url; // Acessa o URL
    window.location.href = receitaAprendizUrl; // Redireciona para a página de detalhes
});

                    // Adiciona o card completo à linha atual
                    row.appendChild(cardReceitaLink);
                });
            })
            .catch(error => {
                console.error('Erro ao buscar receitas:', error);
            });
    }

    searchRecipes();
});