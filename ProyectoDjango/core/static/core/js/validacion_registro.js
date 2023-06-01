var nombre = $("#nombre");
var apellido = $("#apellido");
var clave = $("#contrasena");
var clave1 = $("#contrasena1");
var fono = $("#telefono");
var respuesta = $("#respuesta");
var formulario = $("#formregistro");
var msj = $("#warnings");
var tieneMinuscula = false;
var pattern = /^(?=.*[a-z])(?=.*[A-Z])/;
var patternTel = /^[0-9]*$/;

$(document).ready(function() {
  $("#formregistro").submit(function(e) {
    
    var msjMostrar = "";
    var enviar = false;

    if (nombre.val().trim().length < 4 || nombre.val().trim().length > 20) {
      msjMostrar += "<br>El nombre debe tener entre 4 y 20 caracteres.";
      enviar = true;
    }

    if (!/^[a-zA-Z-á-é-í-ó-ú]*$/.test(nombre.val())) {
      msjMostrar += "<br>El nombre no debe contener números.";
      enviar = true;
    }

    if (correo.val() == "") {
      msjMostrar += "<br>Ingresa un correo.";
      enviar = true;
    }

    if (!validarCorreo(correo.val())) {
      enviar = true;
    }

    if (clave.val() == "") {
      msjMostrar += "<br>Ingresa una contraseña.";
      enviar = true;
    }

    if (fono.val() == "") {
      msjMostrar += "<br>Ingresa un número telefónico.";
      enviar = true;
    }

    if (clave.val().length < 8 || clave.val().length > 25) {
      msjMostrar += "<br>La contraseña debe tener un mínimo de 8 caracteres y un máximo de 25 caracteres.";
      enviar = true;
    }

    var caracteresEspeciales = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    if (!caracteresEspeciales.test(clave.val())) {
      msjMostrar += "<br>Agrega un carácter especial.";
      enviar = true;
    }

    if (!pattern.test(clave.val())) {
      msjMostrar += "<br>La contraseña debe contener minúsculas y mayúsculas.";
      enviar = true;
    }

    if (!/\d/.test(clave.val())) {
      msjMostrar += "<br>Ingresa algún número en la clave.";
      enviar = true;
    }

    if (clave.val() !== clave1.val()) {
      msjMostrar += "<br>Las contraseñas no coinciden.";
      enviar = true;
    }

    if (fono.val().charAt(0) !== "9") {
      msjMostrar += "<br>El primer número debe ser 9.";
      enviar = true;
    }

    if (!patternTel.test(fono.val())) {
      enviar = true;
    }

    if (fono.val().length !== 9) {
      msjMostrar += "<br>Ingresa un número de teléfono válido.";
      enviar = true;
    }

    if (enviar) {
      e.preventDefault();
      $("#warnings").html(msjMostrar);
      
    } else {
      $("#warnings").html("Enviado");
      
    }
  });

  function validarCorreo(correo) {
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regex.test(correo)) {
      return false;
    }

    return true;
  }
});
