const anotacoes = document.querySelectorAll('.botaoAnotacoes-receita')
const removerReceita = document.querySelectorAll('.botaoRemover-receita')

anotacoes.forEach((e) => {
    e.addEventListener('click', () => {
        document.querySelector('.notas').style.display = 'block'

        const salvar = document.querySelector('#salvar')
        const x = document.querySelector('#x')

        salvar.addEventListener('click', () => {
            document.querySelector('.notas').style.display = 'none'
        })


        x.addEventListener('click', () => {
            document.querySelector('.notas').style.display = 'none'
        })

    })
})

removerReceita.forEach((e) => {
    e.addEventListener('click', () => {
        document.querySelector('.remover-receita').style.display = 'block'

        const salvar = document.querySelector('.voltar-receita')
        const x = document.querySelector('#icon-x-remover')

        salvar.addEventListener('click', () => {
            document.querySelector('.remover-receita').style.display = 'none'
        })


        x.addEventListener('click', () => {
            document.querySelector('.remover-receita').style.display = 'none'
        })

    })
})
