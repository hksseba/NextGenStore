var correo = document.getElementById("email");
var opcion = document.getElementById("lang");
var respuesta = document.getElementById("respuesta");

const formulario = document.getElementById("formrPregunta");
var msj = document.getElementById("warnings");



formulario.addEventListener('submit',e =>{

    e.preventDefault();
    let msjMostrar = "";
    let enviar = false;

    if(enviar){
        msj.innerHTML = msjMostrar;
    }
    else{
        msj.innerHTML = "Enviado";

    }

    const email = correo.value.trim(); // Obtener el valor del campo de correo electrónico y eliminar espacios en blanco

    if (email != "ga.maneiro@duocuc.cl") {
        msjMostrar = msjMostrar + "<br> El correo no existe en el sistema"
        msj.innerHTML= msjMostrar;   
        return false;        
    }

    if (opcion.value != 2 || respuesta.value != "Miguel") {
        msjMostrar = msjMostrar + "<br> Respuesta incorrecta"
        msj.innerHTML= msjMostrar;   
        return false;        
    }

    else{ msjMostrar = msjMostrar + "<br> Enviado"
        msj.innerHTML= msjMostrar;
        window.location.href = '../html/RestablecerContraseña.html';
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