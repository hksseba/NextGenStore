$(document).ready(function() {
  const formulario = $("#formregistro");
  const msj = $("#warnings");

  formulario.on('submit', function(e) {
    let hayErrores = false; // Variable para controlar si hay errores o no

    function mostrarError(mensaje) {
      msj.html(mensaje);
    }

    function validarCorreo(correo) {
      var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!regex.test(correo)) {
        return false;
      }
      return true;
    }

    // Validar longitud del nombre y apellido
    const nombre = $("#nombre").val();
    if (nombre.trim().length < 4 || nombre.trim().length > 20) {
      mostrarError("El nombre debe tener entre 4 y 20 caracteres.");
      hayErrores = true;
    }

    if (nombre.charAt(0) !== nombre.charAt(0).toUpperCase()) {
      mostrarError("La primera letra del nombre debe ser mayúscula.");
      hayErrores = true;
    }

    if (!nombre.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
      mostrarError("El nombre no debe contener números ni caracteres especiales.");
      hayErrores = true;
    }

    const apellido = $("#apellido").val();
    if (apellido.trim().length < 4 || apellido.trim().length > 20) {
      mostrarError("El apellido debe tener entre 4 y 20 caracteres.");
      hayErrores = true;
    }

    if (apellido.charAt(0) !== apellido.charAt(0).toUpperCase()) {
      mostrarError("La primera letra del apellido debe ser mayúscula.");
      hayErrores = true;
    }

    if (!apellido.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
      mostrarError("El apellido no debe contener números ni caracteres especiales.");
      hayErrores = true;
    }

    const correo = $("#email").val();
    if (validarCorreo(correo)) {
      enviar = true;
    }

    if (correo.trim() === "") {
      mostrarError("Por favor, ingrese su correo electrónico.");
      hayErrores = true;
    }

    const clave = $("#contrasena").val();
    const clave1 = $("#contrasena1").val();
    if (clave.length < 8 || clave.length > 25) {
      mostrarError("La contraseña debe tener entre 8 y 25 caracteres.");
      hayErrores = true;
    }

    if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave)) {
      mostrarError("Agrega un carácter especial a la contraseña.");
      hayErrores = true;
    }

    if (clave !== clave1) {
      mostrarError("Las contraseñas no coinciden.");
      hayErrores = true;
    }

    if (!/\d/.test(clave)) {
      mostrarError("Ingresa al menos un número en la contraseña.");
      hayErrores = true;
    }

    const resp = $("#respuesta").val();
    if (resp.trim() === "") {
      mostrarError("La respuesta no puede estar vacía.");
      hayErrores = true;
    }

    // Si no hay errores, mostrar mensaje de éxito y reiniciar el formulario
    if (hayErrores) {
      e.preventDefault();
    } else {
      mostrarError("Enviado correctamente.");
    }
  });
});
