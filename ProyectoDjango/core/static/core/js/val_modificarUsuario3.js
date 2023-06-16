
const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const fono = document.getElementById("telefono");
const nombredireccion = document.getElementById("direccion");
const numdireccion = document.getElementById("numdireccion");
const formulario = document.getElementById("formregistro3");
const msj = document.getElementById("warnings");
formulario.addEventListener('submit', e => {
  
    let hayErrores = false; // Variable para controlar si hay errores o no
    function mostrarError(mensaje) {
      msj.innerHTML = mensaje;
    }

    function validarDireccion(nombredireccion, numdireccion) {
        if (nombredireccion.trim() === "" || numdireccion.trim() === "") {
          return false; // La dirección o número de dirección están en blanco
        }
        return true; // La dirección y número de dirección son válidos
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
    if (!validarDireccion(nombredireccion, numdireccion)) {
        msjMostrar = msjMostrar + "<br>La dirección o número de dirección están en blanco";
        msj.innerHTML= msjMostrar;
    }
  
    // Si no hay errores, mostrar mensaje de éxito y reiniciar el formulario
    if (hayErrores) {
        e.preventDefault()
      
      } else if(hayErrores == false){
        mostrarError("Enviado correctamente.");
      }
  });