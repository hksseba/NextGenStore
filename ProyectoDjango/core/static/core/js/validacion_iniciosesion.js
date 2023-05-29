var correo = document.getElementById("email");
var clave = document.getElementById("contrasena");

var correo1 = "example@gmail.com";
var clave1 = "Example21."

const formulario = document.getElementById("forminicio");
var msj = document.getElementById("warnings");

// Obtener el formulario y el campo de correo electrónico
const campoEmail = document.getElementById("email");

// Agregar un evento de escucha al formulario al enviar
formulario.addEventListener("submit", function (event) {
 
  let msjMostrar="";
  let enviar = false;



  if (correo.value !== correo1){
    enviar = true;
    msjMostrar = msjMostrar + "<br>Correo no registrado.";
    msj.innerHTML= msjMostrar;
  }else{
    msjMostrar = msjMostrar + "";
    msj.innerHTML= msjMostrar;
  
  }
  if (clave.value !== clave1){
  msjMostrar = msjMostrar + "<br>Clave incorrecta.";
  msj.innerHTML= msjMostrar;
    enviar = true;
  }else{
    msjMostrar = msjMostrar + "";
    msj.innerHTML= msjMostrar;
  
  }
/*   if (validarCorreo(correo)){
    enviar = true;
  }

  // Verificar si la contraseña tiene al menos 8 caracteres
  if (clave.value.length < 8 || clave.value.length > 25) {

    enviar = true;
}
  if (clave.value[0] !== clave.value[0].toUpperCase()) {

  enviar = true;
  

}
// Verificar si la contraseña contiene un carácter especial
var caracteresEspeciales = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
if (!caracteresEspeciales.test(clave.value)) {

    enviar = true;
  
}
// Verificar si la contraseña contiene números y no están seguidos
if (!/\d/.test(clave.value)) {
 
    enviar = true;
}*/
  
 if (enviar == false){
  window.location.href = "PaginaPrincipal.html";
  formulario.reset();
}  

});
function esMayuscula(letra){
  if(letra == letra.toUpperCase()){
      return true;
  }
  else{
      enviar = true;
  }
}

function validarCorreo(correo) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!regex.test(correo)) {
    
    return false;
  }

  return true;
}

