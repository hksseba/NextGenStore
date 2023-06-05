const nombredireccion = document.getElementById("direccion");
const numdireccion = document.getElementById("numdireccion");

var msj = document.getElementById("warnings");


let msjMostrar = "";

function validarDireccion(nombredireccion, numdireccion) {
    if (nombredireccion.trim() === "" || numdireccion.trim() === "") {
      return false; // La dirección o número de dirección están en blanco
    }
    return true; // La dirección y número de dirección son válidos
  }
  
  // Ejemplo de uso

  
  if (validarDireccion(nombredireccion, numdireccion)) {
    msjMostrar = msjMostrar + "<br>Correcto";
    msj.innerHTML= msjMostrar;
  } else {
    msjMostrar = msjMostrar + "<br>La dirección o número de dirección están en blanco";
    msj.innerHTML= msjMostrar;
  }