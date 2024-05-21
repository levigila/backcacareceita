document.addEventListener('DOMContentLoaded', function() {
    // Extrai o ID da receita da URL
    const params = new URLSearchParams(window.location.search);
    const recipeId = localStorage.getItem('receitaId');

    if (recipeId) {
        fetchRecipeDetails(recipeId);
    } else {
        console.error('ID da receita não fornecido.');
    }
});

function fetchRecipeDetails(recipeId) {
    const apiKey = '030af2ba4b0b4a36b82f165e979d4f44'; // Substitua pela sua chave de API da Spoonacular
    const url = `https://api.spoonacular.com/recipes/${recipeId}/information?apiKey=${apiKey}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Falha ao buscar detalhes da receita');
            }
            return response.json();
        })
        .then(data => {
            updateRecipeDetails(data);
        })
        .catch(error => {
            console.error('Erro ao buscar detalhes da receita:', error);
        });
}

function updateRecipeDetails(recipe) {
    // Atualiza a imagem
    document.querySelector('.receita-img-audio img').src = recipe.image;
    document.querySelector('.receita-img-audio img').alt = recipe.title;

    // Atualiza o título
    document.querySelector('.receita-info h1').textContent = recipe.title;

    // Atualiza os ingredientes
    const ingredientesContainer = document.querySelector('.receita-ing ul');
    ingredientesContainer.innerHTML = ''; // Limpa os ingredientes existentes
    recipe.extendedIngredients.forEach(ingrediente => {
        const li = document.createElement('li');
        li.textContent = ingrediente.original;
        ingredientesContainer.appendChild(li);
    });

    const tempoPreparoElement = document.querySelector('.tempo-preparo p');
    if (recipe.readyInMinutes) {
        tempoPreparoElement.textContent = `${recipe.readyInMinutes} min`;
    } else {
        tempoPreparoElement.textContent = 'Tempo não disponível';
    }


    // Atualiza o modo de preparo
    const modoPreparoContainer = document.querySelector('.receita-modo-prep ul');
    modoPreparoContainer.innerHTML = ''; // Limpa os passos existentes
    if (recipe.instructions) {
        const instructions = recipe.instructions.split('\n').filter(instruction => instruction.trim() !== '');
        instructions.forEach(instruction => {
            const li = document.createElement('li');
            li.textContent = instruction;
            modoPreparoContainer.appendChild(li);
        });
    } else {
        modoPreparoContainer.innerHTML = '<li>Instruções não disponíveis.</li>';
    }
}