document.querySelector('form').addEventListener('submit', function(event) {
    // Obtén los valores de los campos de contraseña
    var pwd = document.getElementById('pwd').value;
    var pwdConfirm = document.getElementById('pwd-confirm').value;

    // Compara las contraseñas
    if (pwd !== pwdConfirm) {
        // Si las contraseñas no coinciden, muestra un mensaje y evita el envío del formulario
        alert('Las contraseñas no coinciden.');
        event.preventDefault();
    }
});