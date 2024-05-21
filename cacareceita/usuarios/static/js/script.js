document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const suggestionsBox = document.getElementById('suggestions');
    const apiKey = 'db4f0300aaae4a9aa8f4f1aa809aaa55'; // Substitua pela sua chave de API da Spoonacular

    // Função para exibir sugestões de ingredientes
    searchInput.addEventListener('input', function () {
        const query = searchInput.value.trim();
        if (query.length > 0) {
            fetch(`https://api.spoonacular.com/food/ingredients/autocomplete?query=${query}&number=10&apiKey=${apiKey}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(item => {
                            const div = document.createElement('div');
                            div.textContent = item.name;
                            div.classList.add('suggestion-item');
                            div.addEventListener('click', () => {
                                addIngredient(item.name);
                            });
                            suggestionsBox.appendChild(div);
                        });
                        suggestionsBox.style.display = 'block';
                    } else {
                        suggestionsBox.style.display = 'none';
                    }
                });
        } else {
            suggestionsBox.style.display = 'none';
        }
    });

    // Função para adicionar um ingrediente selecionado
    function addIngredient(ingredient) {
        const ingredientesContainer = document.querySelector('.opcoes-ingredientes .opcoes');
        const button = document.createElement('button');
        button.textContent = ingredient;
        ingredientesContainer.appendChild(button);
        suggestionsBox.style.display = 'none';
        searchInput.value = '';
        searchRecipes();
    }

    // Função para buscar receitas com base nos ingredientes selecionados
    function searchRecipes() {
        const recipesContainer = document.querySelector('.receitas-aprendiz .conteudo-receitas');
        recipesContainer.innerHTML = ''; // Limpa o conteúdo atual

        const ingredients = Array.from(document.querySelectorAll('.opcoes-ingredientes .opcoes button'))
            .map(button => button.textContent)
            .join(',');

        fetch(`https://api.spoonacular.com/recipes/findByIngredients?ingredients=${ingredients}&number=12&apiKey=${apiKey}`)
            .then(response => response.json())
            .then(data => {
                // Iterar sobre as receitas para organizá-las em linhas
                let currentRow;
                data.forEach((recipe, index) => {
                    // A cada 3 receitas, cria uma nova linha
                    if (index % 3 === 0) {
                        currentRow = document.createElement('div');
                        currentRow.classList.add('linha-cardReceita');
                        recipesContainer.appendChild(currentRow);
                    }

                    // Cria a cardReceita
                    const cardReceita = document.createElement('div');
                    cardReceita.classList.add('cardReceita');

                    // Conteúdo da cardReceita
                    // const caixaEtiqueta = document.createElement('div');
                    // caixaEtiqueta.classList.add('caixaEtiqueta-receita');
                    // const etiqueta = document.createElement('img');
                    // etiqueta.classList.add('etiquetaReceita');
                    // etiqueta.src = recipe.image;
                    // caixaEtiqueta.appendChild(etiqueta);
                    // cardReceita.appendChild(caixaEtiqueta);

                    const imagemReceita = document.createElement('img');
                    imagemReceita.classList.add('foto-receita');
                    imagemReceita.src = recipe.image;
                    cardReceita.appendChild(imagemReceita);

                    const tituloReceita = document.createElement('p');
                    tituloReceita.textContent = recipe.title;
                    cardReceita.appendChild(tituloReceita);

                    // const avaliacaoReceita = document.createElement('div');
                    // avaliacaoReceita.classList.add('avaliacao-receita');
                    // for (let i = 0; i < 5; i++) {
                    //     const estrela = document.createElement('img');
                    //     estrela.classList.add('estrelinha');
                    //     estrela.src = 'estrelinha';
                    //     avaliacaoReceita.appendChild(estrela);
                    // }
                    // cardReceita.appendChild(avaliacaoReceita);

                    // Adiciona a cardReceita à linha atual
                    currentRow.appendChild(cardReceita);
                });
            })
            .catch(error => {
                console.error('Erro ao buscar receitas:', error);
            });
    }

    // Inicializa com uma busca padrão ou limpa o conteúdo ao carregar a página
    searchRecipes();
});
