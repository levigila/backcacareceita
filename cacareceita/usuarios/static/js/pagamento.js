const checkboxes = document.querySelectorAll('.pagamento input[type="checkbox"]');

const checkboxesCartao = document.querySelectorAll('.tipo-cartao input[type="checkbox"]');
const pagamento = document.querySelector('#continuar')
var Formapagamento = 0

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        checkboxes.forEach(cb => {
            if (cb !== this) {
                cb.checked = false;      
            }
        });
    });
});

checkboxesCartao.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        checkboxesCartao.forEach(cb => {
            if (cb !== this) {
                cb.checked = false;
            }
        });
    });
});

pagamento.addEventListener('click', () => {
    checkboxes.forEach(checked => {
        if (checked.checked){
            if(checked.id !== 'boleto'){
                const divPagamento = document.querySelector(`.${checked.id}`)

                divPagamento.style.display = 'flex'
            }
        }
    })
})