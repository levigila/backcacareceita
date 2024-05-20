document.addEventListener('DOMContentLoaded', function () {
    var favoritarButtons = document.querySelectorAll('.favoritar');

    favoritarButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var receitaId = this.dataset.receitaId;
            // Enviar requisição para favoritar receita
            fetch('/favoritar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ receita_id: receitaId })
            }).then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Receita favoritada com sucesso!');
                } else {
                    console.log('Erro ao favoritar a receita.');
                }
            }).catch(error => {
                console.error('Erro:', error);
            });
        });
    });

    // Função para obter o CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
