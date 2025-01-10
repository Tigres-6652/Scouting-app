// static/main.js

// Seleccionar el ícono y el menú
const menuIcon = document.getElementById('menu-icon');
const fullscreenMenu = document.getElementById('fullscreen-menu');

// Alternar la clase para mostrar/ocultar el menú
menuIcon.addEventListener('click', () => {
    fullscreenMenu.classList.toggle('hidden');
});

document.addEventListener('DOMContentLoaded', () => {
    const image = document.getElementById('main-image');

    // Agregar la clase para expandir la imagen
    setTimeout(() => {
        image.classList.add('expand');
    }, 500); // Retraso opcional para ver el efecto
});
