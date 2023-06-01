$(document).ready(function() {
    var nombre = $("#nombre");
    var apellido = $("#apellido");
    var clave = $("#contrasena");
    var clave1 = $("#contrasena1");
    var correo = $("#email");
    var fono = $("#telefono");
    var resp = $("#respuesta");
    var formulario = $("#formregistro");
    var msj = $("#warnings");
    var tieneMinuscula = false;
    var pattern = /^(?=.*[a-z])(?=.*[A-Z])/;
    var patternTel = /^[0-9]*$/;
  
    formulario.on("submit", function(e) {
      var msjMostrar = "";
      var enviar = false;
  
      if (
        nombre.val().trim() === "" ||
        apellido.val().trim() === "" ||
        clave.val().trim() === "" ||
        clave1.val().trim() === "" ||
        correo.val().trim() === "" ||
        fono.val().trim() === "" ||
        resp.val().trim() === ""
      ) {
        msjMostrar = "Por favor, complete todos los campos.";
      } else if (
        (nombre.val().trim().length < 4 || nombre.val().trim().length > 20) ||
        (apellido.val().trim().length < 4 || apellido.val().trim().length > 20) ||
        !nombre.val().trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/) ||
        !apellido.val().trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/) ||
        !validarCorreo(correo.val().trim()) ||
        clave.val().length < 8 || clave.val().length > 25 ||
        !/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.val()) ||
        !clave.val().match(pattern) ||
        !/\d/.test(clave.val()) ||
        clave.val() !== clave1.val() ||
        fono.val().charAt(0) !== "9" ||
        fono.val().length !== 9 ||
        !patternTel.test(fono.val().trim())
      ) {
        if (nombre.val().trim().length < 4 || nombre.val().trim().length > 20) {
          msjMostrar += "<br>El nombre debe tener entre 4 y 20 caracteres.";
        }
        if (apellido.val().trim().length < 4 || apellido.val().trim().length > 20) {
          msjMostrar += "<br>El apellido debe tener entre 4 y 20 caracteres.";
        }
        if (!nombre.val().trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/)) {
          msjMostrar += "<br>El nombre no debe contener números.";
        }
        if (!apellido.val().trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/)) {
          msjMostrar += "<br>El apellido no debe contener números.";
        }
        if (!validarCorreo(correo.val().trim())) {
          msjMostrar += "<br>Ingresa un correo válido.";
        }
        if (clave.val().length < 8 || clave.val().length > 25) {
          msjMostrar += "<br>La contraseña debe tener entre 8 y 25 caracteres.";
        }
        if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.val())) {
          msjMostrar += "<br>Agrega un carácter especial a la contraseña.";
        }
        if (!clave.val().match(pattern)) {
          msjMostrar += "<br>La contraseña debe contener minúsculas y mayúsculas.";
        }
        if (!/\d/.test(clave.val())) {
          msjMostrar += "<br>Ingresa al menos un número en la contraseña.";
        }
        if (clave.val() !== clave1.val()) {
          msjMostrar += "<br>Las contraseñas no coinciden.";
        }
        if (fono.val().charAt(0) !== "9") {
          msjMostrar += "<br>El primer número del teléfono debe ser 9.";
        }
        if (fono.val().length !== 9) {
          msjMostrar += "<br>Ingresa un número de teléfono válido (9 dígitos).";
        }
      } else {
        msjMostrar = "<br>Enviado correctamente.";
        enviar = true;
        formulario.trigger("reset");
      }
  
      msj.html(msjMostrar);
  
      if (!enviar) {
        e.preventDefault();
      }
    });
  
    function validarCorreo(correo) {
      var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(correo);
    }
  });
  