// Variables para los elementos del formulario
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const clave = document.getElementById("contrasena");
const clave1 = document.getElementById("contrasena1");
const correo = document.getElementById("email");
const fono = document.getElementById("telefono");
const resp = document.getElementById("respuesta");
const formulario = document.getElementById("formregistro");
const msj = document.getElementById("warnings");

// Expresiones regulares
const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?])/;
const patternTel = /^[0-9]{9}$/;

// Función para validar el correo electrónico
function validarCorreo(correo) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(correo);
}

// Función para mostrar mensajes de error
function mostrarError(mensaje) {
  msj.innerHTML = mensaje;
}

// Función para limpiar los mensajes de error
function limpiarErrores() {
  msj.innerHTML = "";
}

// Función para validar el formulario al enviarlo
formulario.addEventListener('submit', function(e) {
  e.preventDefault(); // Evitar el envío del formulario

  // Limpiar mensajes de error previos
  limpiarErrores();

  // Bandera para indicar si hay errores
  let hayErrores = false;

  // Validar campos requeridos
  if (
    nombre.value.trim() === "" ||
    apellido.value.trim() === "" ||
    clave.value.trim() === "" ||
    clave1.value.trim() === "" ||
    correo.value.trim() === "" ||
    fono.value.trim() === "" ||
    resp.value.trim() === ""
  ) {
    mostrarError("Por favor, complete todos los campos.");
    hayErrores = true;
  }

  // Validar longitud del nombre y apellido
  if (nombre.value.trim().length < 4 || nombre.value.trim().length > 20) {
    mostrarError("El nombre debe tener entre 4 y 20 caracteres.");
    hayErrores = true;
  }

  if (!nombre.value.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
    mostrarError("El nombre no debe contener números ni caracteres especiales.");
    hayErrores = true;
  }

  if (apellido.value.trim().length < 4 || apellido.value.trim().length > 20) {
    mostrarError("El apellido debe tener entre 4 y 20 caracteres.");
    hayErrores = true;
  }

  if (!apellido.value.trim().match(/^[a-zA-ZáéíóúÁÉÍÓÚ\s-]*$/)) {
    mostrarError("El apellido no debe contener números ni caracteres especiales.");
    hayErrores = true;
  }

  // Validar formato de correo electrónico
  if (!validarCorreo(correo.value.trim())) {
    mostrarError("Ingresa un correo válido.");
    hayErrores = true;
  }

  // Validar longitud y formato de contraseña
  if (clave.value.length < 8 || clave.value.length > 25) {
    mostrarError("La contraseña debe tener entre 8 y 25 caracteres.");
    hayErrores = true;
  }

  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.value)) {
    mostrarError("Agrega un carácter especial a la contraseña.");
    hayErrores = true;
  }

  if (!clave.value.match(pattern)) {
    mostrarError("La contraseña debe contener minúsculas, mayúsculas, números y caracteres especiales.");
    hayErrores = true;
  }

  if (!/\d/.test(clave.value)) {
    mostrarError("Ingresa al menos un número en la contraseña.");
    hayErrores = true;
  }

  // Validar coincidencia de contraseñas
  if (clave.value !== clave1.value) {
    mostrarError("Las contraseñas no coinciden.");
    hayErrores = true;
  }

  // Validar número de teléfono
  if (!fono.value.startsWith("9") || !patternTel.test(fono.value)) {
    mostrarError("Ingresa un número de teléfono válido (9 dígitos) que comience con 9.");
    hayErrores = true;
  }

  // Si no hay errores, mostrar mensaje de éxito y reiniciar el formulario
  if (!hayErrores) {
    mostrarError("Enviado correctamente.");
    formulario.reset();
  }
});
