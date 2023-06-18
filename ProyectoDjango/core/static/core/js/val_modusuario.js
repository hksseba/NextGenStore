$(document).ready(function() {
  const formulario = $("#formUser");
  const msj = $("#warnings");

  formulario.on('submit', function(e) {
    let hayErrores = false; // Variable para controlar si hay errores o no

    function mostrarError(mensaje) {
      msj.html(mensaje);
    }


    // Validar longitud del nombre y apellido
    const nombre = $("#nombre").val();
    const apellido = $("#apellido").val();
    const telefono = $("#telefono").val();
    const nombredireccion = $("#direccion").val();
    const numdireccion = $("#numdireccion").val();

    if (nombre.trim().length < 4 || nombre.trim().length > 20) {
      mostrarError("El nombre debe tener entre 4 y 20 caracteres.");
      hayErrores = true;
    }

    if (!nombre.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
      mostrarError("El nombre no debe contener números ni caracteres especiales.");
      hayErrores = true;
    }

    if (apellido.trim().length < 4 || apellido.trim().length > 20) {
      mostrarError("El apellido debe tener entre 4 y 20 caracteres.");
      hayErrores = true;
    }

    if (!apellido.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
      mostrarError("El apellido no debe contener números ni caracteres especiales.");
      hayErrores = true;
    }

    if( nombredireccion.trim() === "" ||  numdireccion.trim() === "" ){
      mostrarError("Ingrese una calle y un numero.");
      hayErrores = true;
    }

    if(telefono.trim() === ""){
      mostrarError("Ingrese un numero.");
      hayErrores = true;
    }
   
    if (/\D/.test(telefono)) {
      mostrarError("El número no puede contener letras.");
      hayErrores = true;
    }
    
    if (hayErrores) {
      e.preventDefault();
    
    } else {
      mostrarError("Enviado correctamente.");
    }
  });
});
