const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const clave = document.getElementById("contrasena");
const clave1 = document.getElementById("contrasena1");
const correo = document.getElementById("email");
const fono = document.getElementById("telefono");
const resp = document.getElementById("respuesta");
const formulario = document.getElementById("formregistro");
const msj = document.getElementById("warnings");
formulario.addEventListener('submit', e => {
  
    let hayErrores = false; // Variable para controlar si hay errores o no
    function mostrarError(mensaje) {
      msj.innerHTML = mensaje;
    }
    function validarCorreo(correo) {
      var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
      if (!regex.test(correo)) {
        
        return false;
      }
    
      return true;
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
    if (validarCorreo(correo)){
      enviar = true;
    }
    if (correo.value.trim() === "") {
      mostrarError("Por favor, ingrese su correo electrónico.");
      hayErrores = true;
    }
    if (clave.value.length < 8 || clave.value.length > 25) {
      mostrarError("La contraseña debe tener entre 8 y 25 caracteres.");
      hayErrores = true;
    }
    if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(clave.value)) {
      mostrarError("Agrega un carácter especial a la contraseña.");
      hayErrores = true;
    }
    if (clave.value !== clave1.value) {
      mostrarError("Las contraseñas no coinciden.");
      hayErrores = true;
    }
    if (!/\d/.test(clave.value)) {
      mostrarError("Ingresa al menos un número en la contraseña.");
      hayErrores = true;
    }
    if(resp.value.trim() === ""){
      mostrarError("La respuesta no puede estar vacia.");
      hayErrores = true;

    }
  
    // Si no hay errores, mostrar mensaje de éxito y reiniciar el formulario
    if (hayErrores) {
        e.preventDefault()
      
      } else if(hayErrores == false){
        mostrarError("Enviado correctamente.");
      }
  });
  