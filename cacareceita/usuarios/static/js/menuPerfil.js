const menu = document.querySelector('#menu-perfil')


menu.addEventListener('click', () => {
    const divMenu = document.querySelector('.menu-perfil')
    divMenu.classList.toggle('show-perfil')
})