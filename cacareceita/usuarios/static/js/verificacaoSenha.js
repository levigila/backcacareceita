const inputs = document.querySelectorAll('.otp input')

inputs.forEach((input, index) => {
    input.dataset.index = index;
    input.addEventListener('paste', pasteHandle);
    input.addEventListener('keyup', handle)
})

function pasteHandle(e) {
    var data = e.clipboardData.getData("text")
    const value = data.split("")
    if (value.length === inputs.length) {
        inputs.forEach((input, index) => {
            input.value = value[index]
            GO()
        })
    }
}

function handle(e) {
    const input = e.target
    var value = input.value
    input.value = value ? value[0] : "";

    let fieldIndex = input.dataset.index
    if (value.length > 0 && fieldIndex < inputs.length - 1) {
        input.nextElementSibling.focus()
    }

    if (e.key == "Backspace" && fieldIndex > 0) {
        input.previousElementSibling.focus()
    }

    if (fieldIndex == input.length - 1) {
        GO()
    }

}

function GO() {
    var value = "";

    inputs.forEach(input => {
        value += input.value
        input.disabled = true
    })

    console.log("VALUE: " + value)
}

document.querySelector(".form-otp").addEventListener("submit", function (event) {
    // Impedindo o comportamento padrão de envio do formulário
    event.preventDefault();

    const inputs = document.querySelectorAll('.otpInput')
    const cod = `${inputs[0].value}${inputs[1].value}${inputs[2].value}${inputs[3].value}`

    if (!isNaN(cod) && cod.length === 4) {
        this.setAttribute("action", "http://127.0.0.1:8000/auth/verificaoSenha/");

        this.setAttribute("method", "post");

        this.submit();

        return
    }

    return window.location.reload();
});


