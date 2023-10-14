if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitud = position.coords.latitude;
        var longitud = position.coords.longitude;

        // Mostrar la latitud y longitud en la página
        document.getElementById("latitud").textContent = latitud;
        document.getElementById("longitud").textContent = longitud;

        // Crear un objeto con los datos a enviar en formato JSON
        var data = {
            idcliente: 1,
            latitud: latitud,
            longitud: longitud
        };

        // Configurar encabezados para enviar JSON
        var config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        // Realizar una solicitud POST a la API en Python
        axios.post('api/saveruta', JSON.stringify(data), config)
            .then(function (response) {
                console.log('Datos enviados con éxito:', response.data);
            })
            .catch(function (error) {
                console.error('Error al enviar datos:', error);
            });
    });
} else {
    console.log("El navegador no admite la geolocalización.");
}


function saveusuario(){
    let var_nombre= document.getElementById('usuario_registrar');
    let var_password=document.getElementById('password_registrar')
    var data = {
        nombre_usuario: var_nombre.value,
        contraseña: var_password.value

    };

    var config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    let ruta= 'api/saveusuario'

   
    axios.post(ruta, JSON.stringify(data), config)
    .then(function (response) {
        var_nombre.value="";
        var_password.value="";
        console.log('respuesta del backend:', response.data);
        alertify.alert(response.data, function(){
    alertify.message(response.data);
  });
    })
    .catch(function (error) {
        console.error('Error al enviar datos:', error);
    });

}


function get_usuario() {
    let var_nombre = document.getElementById('usuario');
    let var_password = document.getElementById('password');

    let data = {
        
        nombre_usuario: var_nombre.value,
        contraseña: var_password.value
    };
    

    let config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    let ruta = 'api/iniciar_sesion';

    axios.post(ruta, JSON.stringify(data), config)
        .then(function (response) {
            
            var_nombre.value = "";
            var_password.value = "";
            console.log('Respuesta del backend:', response.data);

            if (response.data.valid) {
                alertify.success(response.data.message);
                
                window.location.href = 'index'; 
                

                
              
                

            } else {
                alertify.error(response.data.message);
                // Realizar acciones adicionales para el inicio de sesión fallido
            }
        })
        .catch(function (error) {
            console.error('Error al enviar datos:', error);
        });
}
