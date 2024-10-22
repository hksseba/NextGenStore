 $(document).ready(function () {
    $("#formProducto").submit(function (e) {
      var nombreProducto = $("#nombreProducto").val();
      var stock = $("#StockProducto").val();
      var precio = $("#Precio").val();
      var foto = $("#fotoProducto").val();
      let msjMostrar = "";
      let enviar = false;
      const pattern = /^[a-zA-Z0-9-á-é-í-ó-ú ]*$/;
  
        if (
          foto === ""){
          msjMostrar += "Debe ingresar foto del producto ";  
          enviar = true;
        }
        
        if (
            nombreProducto == ""){
            msjMostrar += "<br>Debe ingresar el nombre del producto ";  
            enviar = true;
            }

        if (!pattern.test(nombreProducto)){
            msjMostrar += "<br>El nombre no puede contener caracteres especiales";
            enviar = true;
           }
           
        if (!esMayuscula(nombreProducto.trim().charAt(0))  ){
            msjMostrar += "<br>El nombre debe comenzar con mayúscula";
            enviar = true
           }

        if (precio == "" || precio < 1) {
          msjMostrar += "<br>Debe ingresar el precio del producto ";
          enviar = true;
        }
        
        if (stock == "" || stock < 1) {
          msjMostrar += "<br>Debe ingresar el stock del producto ";
          enviar = true;
        }


      if (enviar) {
        $("#warnings").html(msjMostrar);
        e.preventDefault();
      } else {
        $("#warnings").html("Enviado");
        
      }
    });
  
    function esMayuscula(letra) {
      if (letra == letra.toUpperCase()) {
        return true;
      } else {
        return false;
      }
    }
  });