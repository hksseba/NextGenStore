var nombre = document.getElementById("nombre");
var apellido = document.getElementById("apellido");
var clave = document.getElementById("contrasena");
var clave1 = document.getElementById("contrasena1");
var correo = document.getElementById("email");
var fono = document.getElementById("telefono");
var resp = document.getElementById("respuesta");
const formulario = document.getElementById("formregistro");
var msj = document.getElementById("warnings");
var tieneMinuscula = false;
const pattern = /^(?=.*[a-z])(?=.*[A-Z])/
const patternTel = /^[0-9]*$/;

formulario.addEventListener('submit', e => {
  let msjMostrar = "";
  let enviar = false;

  if (
    nombre.value.trim() === "" ||
    apellido.value.trim() === "" ||
    clave.value.trim() === "" ||
    clave1.value.trim() === "" ||
    correo.value.trim() === "" ||
    fono.value.trim() === "" ||
    resp.value.trim() === ""
  ) {
    msjMostrar = "Por favor, complete todos los campos.";
    enviar = true;
  } else if (
    nombre.value.trim().length < 4 ||
    nombre.value.trim().length > 20 ||
    apellido.value.trim().length < 4 ||
    apellido.value.trim().length > 20 ||
    !nombre.value.trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/) ||
    !apellido.value.trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/) ||
    !validarCorreo(correo.value.trim()) ||
    clave.value.length < 8 ||
    clave.value.length > 25 ||
    !/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.value) ||
    !clave.value.match(pattern) ||
    !/\d/.test(clave.value) ||
    clave.value !== clave1.value ||
    fono.value.charAt(0) !== "9" ||
    fono.value.length !== 9 ||
    !patternTel.test(fono.value.trim())
  ) {
    enviar = true;
    if (nombre.value.trim().length < 4 || nombre.value.trim().length > 20) {
      msjMostrar += "<br>El nombre debe tener entre 4 y 20 caracteres.";
    }
    if (apellido.value.trim().length < 4 || apellido.value.trim().length > 20) {
      msjMostrar += "<br>El apellido debe tener entre 4 y 20 caracteres.";
    }
    if (!nombre.value.trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/)) {
      msjMostrar += "<br>El nombre no debe contener números.";
    }
    if (!apellido.value.trim().match(/^[a-zA-Z-á-é-í-ó-ú]*$/)) {
      msjMostrar += "<br>El apellido no debe contener números.";
    }
    if (!validarCorreo(correo.value.trim())) {
      msjMostrar += "<br>Ingresa un correo válido.";
    }
    if (clave.value.length < 8 || clave.value.length > 25) {
      msjMostrar += "<br>La contraseña debe tener entre 8 y 25 caracteres.";
    }
    if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.value)) {
      msjMostrar += "<br>Agrega un carácter especial a la contraseña.";
    }
    if (!clave.value.match(pattern)) {
      msjMostrar += "<br>La contraseña debe contener minúsculas y mayúsculas.";
    }
    if (!/\d/.test(clave.value)) {
      msjMostrar += "<br>Ingresa al menos un número en la contraseña.";
    }
    if (clave.value !== clave1.value) {
      msjMostrar += "<br>Las contraseñas no coinciden.";
    }
    if (fono.value.charAt(0) !== "9") {
      msjMostrar += "<br>El primer número del teléfono debe ser 9.";
    }
    if (fono.value.length !== 9) {
      msjMostrar += "<br>Ingresa un número de teléfono válido (9 dígitos).";
    }
  } else {
    msjMostrar = "<br>Enviado correctamente.";
    formulario.reset();
  }

  msj.innerHTML = msjMostrar;

  if (enviar) {
    e.preventDefault();
  }
});

function validarCorreo(correo) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(correo);
}
