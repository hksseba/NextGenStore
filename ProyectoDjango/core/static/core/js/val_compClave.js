$(document).ready(function() {
    const formulario = $("#formrPregunta");
    const msj = $("#warnings");

    formulario.on('submit', function(e) {
      let hayErrores = false; // Variable para controlar si hay errores o no

      function mostrarError(mensaje) {
        msj.html(mensaje);
      }

      function validarCorreo(correo) {
        var regex = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
        if (!regex.test(correo)) {
          return false;
        }
        return true;
      }

      const correo = $("#email").val();
      if (validarCorreo(correo)) {
        enviar = true;
      }

      if (correo.trim() === "") {
        mostrarError("Por favor, ingrese su correo electrónico.");
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