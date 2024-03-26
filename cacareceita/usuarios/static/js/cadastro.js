document.getElementById("cadastroForm").addEventListener("submit", function (event) {
    event.preventDefault()

    const user = document.getElementById("user").value
    const passwordConfirm = document.getElementById("password-confirm").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const statusLogin = document.getElementById("status-cadastro")

    document.querySelector('.pop-up').style.display = 'block'
    document.querySelector('.test').style.display = 'block'

    statusLogin.innerText = 'E-mail ou senha invalidos '
    setTimeout(() => {
        document.querySelector('.pop-up').style.display = 'none'
        document.querySelector('.test').style.display = 'none'
    }, 2000);

    if(password !== passwordConfirm) {
        document.querySelector('.pop-up').style.display = 'block'
        document.querySelector('.test').style.display = 'block'

        statusLogin.innerText = 'As senhas não coincidem'
        setTimeout(() => {
            document.querySelector('.pop-up').style.display = 'none'
            document.querySelector('.test').style.display = 'none'
        }, 2000);
    } else {
        document.querySelector('.pop-up').style.display = 'block'
        document.querySelector('.test').style.display = 'block'

        statusLogin.innerText = 'Usuário cadastrado com sucesso!'
        setTimeout(() => {
            document.querySelector('.pop-up').style.display = 'none'
            document.querySelector('.test').style.display = 'none'
        }, 2000);
    }


});

function validateFields() {
    const user = document.getElementById("user").value
    const passwordConfirm = document.getElementById("password-confirm").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    if (!user || !password || !email || !passwordConfirm) {
        document.getElementById('entrar').disabled = true;
    } else {
        document.getElementById('entrar').disabled = false;
    }
}
