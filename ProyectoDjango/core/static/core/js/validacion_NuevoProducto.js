$(document).ready(function () {
    $("#formProducto").submit(function (e) {
        e.preventDefault();
        var nombreProducto = $("#nombreProducto").val();
        var stock = $("#StockProducto").val();
        var precio = $("#Precio").val();

        let msjMostrar = "";
        let enviar = false;
        const pattern = /^[a-zA-Z0-9-á-é-í-ó-ú ]*$/;

        if(nombreProducto == ""  ){
            msjMostrar = msjMostrar + "Debe ingresar el nombre del producto ";
            enviar = true;
        }
         
        if(pattern.test(nombreProducto)){

        }
        else{msjMostrar += "<br>El nombre no puede contener caracteres especiales";
        enviar = true;
        }

        var letra = nombreProducto.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrar += "<br>El nombre debe comenzar con mayúscula";
            enviar = true;
        }
        

        if(stock =="" || stock <1 ){
            msjMostrar = msjMostrar + "<br>Debe ingresar el stock del producto ";
            enviar = true;
            
        }
        if(precio == "" || precio <1){
            msjMostrar = msjMostrar + "<br>Debe ingresar el precio del producto ";
            enviar = true;
        }

        if(enviar){
            $("#warnings").html(msjMostrar);
        }
        else{
            $("#warnings").html("Enviado");
            $('input[type="text"]').val('');
            $('input[type="number"]').val('');
            $(location).attr('href','../html/PovAdmin.html');
        }

    });
    function esMayuscula(letra){

        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
    }

});