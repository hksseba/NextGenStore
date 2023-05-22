var nombre = document.getElementById("nombre");
var clave = document.getElementById("contrasena");
var clave1 = document.getElementById("rcontrasena");


const formulario = document.getElementById("formrContrasena");
var msj = document.getElementById("warnings");
var tieneMinuscula = false;
const pattern = /^(?=.*[a-z])(?=.*[A-Z])/

formulario.addEventListener('submit',e =>{

    
    let msjMostrar = "";

    
    
    let enviar = false;

  if(clave.value == ""  ){
      msjMostrar = msjMostrar + "<br>Ingresa una contraseña";
      msj.innerHTML= msjMostrar;
      enviar = true;
    } 


        
        // Verificar si la contraseña tiene al menos 8 caracteres
        if (clave.value.length < 8 || clave.value.length > 25 ) {
            msjMostrar = msjMostrar + "<br> La contraseña debe tener un minimo 8 caracteres y un maximo de 25 caracteres "
            msj.innerHTML= msjMostrar;
            enviar = true;
        }
      
        // Verificar si la contraseña contiene un carácter especial
        var caracteresEspeciales = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
        if (!caracteresEspeciales.test(clave.value)) {
            msjMostrar = msjMostrar + "<br> Agrega un caracter especial"
            msj.innerHTML= msjMostrar;
            enviar = true;
        }
      
        if(pattern.test(clave.value)){

        }
        else{msjMostrar = msjMostrar + "<br> La contraseña debe contener minusculas y mayusculas"
        msj.innerHTML= msjMostrar;
        enviar = true;
        }

        

        // Verificar si la contraseña contiene números y no están seguidos
        if (!/\d/.test(clave.value)) {
            msjMostrar = msjMostrar + "<br> Ingresa algun numero en la clave"
            msj.innerHTML= msjMostrar;
            enviar = true;
        }
        if (clave.value !== clave1.value) {
          msjMostrar = msjMostrar + "<br> Las contraseñas no coinciden."
          msj.innerHTML= msjMostrar;
          enviar = true;
        }
        
          if (enviar == false){
            msjMostrar = msjMostrar + "<br> enviado"
            msj.innerHTML= msjMostrar;
            window.location.href = "InicioSesion.html";   
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