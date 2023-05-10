var nombre = document.getElementById("nombre");
var clave = document.getElementById("contrasena");
var clave1 = document.getElementById("contrasena1");
var fono = document.getElementById("telefono");
const formulario = document.getElementById("formregistro");
var msj = document.getElementById("warnings");
var tieneMinuscula = false;
const pattern = /^(?=.*[a-z])(?=.*[A-Z])/
const patternTel = /^[0-9]*$/;

formulario.addEventListener('submit',e =>{

    e.preventDefault();
    let msjMostrar = "";

    
    
    let enviar = false;
    if(nombre.value.trim().length < 4 || nombre.value.trim().length > 20){
        msjMostrar = msjMostrar + "<br>El nombre debe tener entre 4 y 20 caracteres.";
        enviar = true;       
    }
    const regex = /^[a-zA-Z-á-é-í-ó-ú]*$/;
    if(regex.test(nombre.value)){

    }else{
      msjMostrar = msjMostrar + "<br>El nombre no debe contener numeros";
      msj.innerHTML = msjMostrar;
      enviar = true;
    }

    if(correo.value == ""  ){
      msjMostrar = msjMostrar + "<br>Ingresa un correo";
      msj.innerHTML= msjMostrar;
      enviar = true;
  }else{
    msjMostrar = msjMostrar + "";
    msj.innerHTML= msjMostrar;
  
  }
  if (validarCorreo(correo)){
    enviar = true;
  }
  
  if(clave.value == ""  ){
      msjMostrar = msjMostrar + "<br>Ingresa una contraseña";
      msj.innerHTML= msjMostrar;
      enviar = true;
    }
    if(fono.value == ""  ){
      msjMostrar = msjMostrar + "<br>Ingresa un numero telefonico";
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
        
          if (fono.value.charAt(0) !== "9") {
            enviar = true;
            msjMostrar = msjMostrar + "<br> El primer numero debe ser 9"
            msj.innerHTML= msjMostrar;
            enviar = true;
          } 
          if(patternTel.test(fono.value)){

          }
        
          // Verificar si el número de teléfono tiene un máximo de 9 dígitos
        if (fono.value.length !== 9) {
            msjMostrar = msjMostrar + "<br> Ingresa un numero de telefono valido"
            msj.innerHTML= msjMostrar;
            enviar = true;
          }
          if (enviar == false){
            msjMostrar = msjMostrar + "<br> enmviadooodoasodsaodas"
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

    function validarCorreo(correo) {
      var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
      if (!regex.test(correo)) {
        
        return false;
      }
    
      return true;
    }