const login = 'viipaxx'
const senha = '@123'

document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault()

    const user = document.getElementById("user").value
    const password = document.getElementById("password").value
    const statusLogin = document.getElementById("status-login")


    if (user.toLowerCase() !== login.toLocaleLowerCase() && password !== senha) {
        
        document.querySelector('.pop-up').style.display = 'block'
        document.querySelector('.blur').style.display = 'block'

        statusLogin.innerText = 'E-mail ou senha invalidos '
        setTimeout(() => {   
            document.querySelector('.pop-up').style.display = 'none'
            document.querySelector('.blur').style.display = 'none'
        }, 2000);
        
    }else {
        return window.location.href = 'https://youtube.com/results?search_query=parabens'
    }

});

function validateFields() {
    const user = document.getElementById("user").value
    const password = document.getElementById("password").value

    if (!user || !password) {
        document.getElementById('entrar').disabled = true;
    } else {
        document.getElementById('entrar').disabled = false;
    }
}


function teste() {
    // validateUser()
    // if(validateLogin()){
    //     window.location.href = 'https://youtube.com'
    // }else {
    //     console.log('login errado')
    // }
}

