const menu = document.querySelector('#menu-perfil')
const logout = document.querySelector('#logout')
const voltar = document.querySelectorAll('.voltar')
const blur = document.querySelector('.blur')

menu.addEventListener('click', () => {
    const blur = document.querySelector('.blur')
    const divMenu = document.querySelector('.menu-perfil')

    document.querySelector('body').style.overflow = 'hidden'
    divMenu.classList.add('show-perfil')
    blur.style.display = 'block'
})

voltar.forEach((e) => {
    e.addEventListener('click', () => {
        const blur = document.querySelector('.blur')
        const divMenu = document.querySelector('.menu-perfil')
    
        document.querySelector('.sair').style.display = 'none'
        document.querySelector('body').style.overflow = 'auto'
        divMenu.classList.remove('show-perfil')
        blur.style.display = 'none'
    })
})

blur.addEventListener('click', () => {
    const blurr = document.querySelector('.blur')
    const divMenu = document.querySelector('.menu-perfil')

    document.querySelector('.sair').style.display = 'none'
    document.querySelector('body').style.overflow = 'auto'
    
    divMenu.classList.remove('show-perfil')
    blurr.style.display = 'none'
})

logout.addEventListener('click', () => {
    document.querySelector('.sair').style.display = 'block'
})