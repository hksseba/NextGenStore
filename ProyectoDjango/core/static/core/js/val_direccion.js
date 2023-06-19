$(document).ready(function() {
  var formulario = $("#formdireccion");
  var msj = $("#warnings");

  formulario.on("submit", function(e) {
    
    var nombredireccion = $("#direccion").val().trim();
    var numdireccion = $("#numdireccion").val().trim();
    let hayErrores = false; // Variable para controlar si hay errores o no

    if (nombredireccion === "" || numdireccion === "") {
      mostrarError("Ingrese una calle y un número.");
      hayErrores = true
    } 

    if (hayErrores) {
      e.preventDefault();
      mostrarError
    } else {
      mostrarError("Enviado correctamente.");
    }
  });

  function mostrarError(mensaje) {
    msj.html(mensaje);
  }
});
