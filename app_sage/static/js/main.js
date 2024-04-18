$(document).ready(function () {


    // Evento click para '#generar-1'
    $('#generar-1').on('click', function (event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace.
        consulta1();
    });

    $('#generar-2').on('click', function (event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace.
        consulta_articulos();
    });

    $('#generar-3').on('click', function (event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace.
        consulta_articulos_precio();
    });

    // Repetir para los otros IDs...
    $('#generar-4').on('click', function (event) {
        event.preventDefault();
        consulta_albaran();
    });

    $('#generar-5').on('click', function (event) {
        event.preventDefault();
        consulta_cabecera_albaran();
    });

    // Suponiendo que 'consulta_oferta_cliente' es otra función que tienes.
    $('#generar-6').on('click', function (event) {
        event.preventDefault();
        consulta_oferta_cliente();
    });

    // Para asegurar que los manejadores de eventos se añadan a elementos dinámicos,
    // podrías delegar el evento desde un contenedor estático, algo así:
    $('.dropdown-menu').on('click', 'a.dropdown-item', function (event) {
        event.preventDefault();
        var actionId = $(this).attr('id');
        switch (actionId) {
            case 'generar-1':
                consulta1();
                break;
            case 'generar-4':
                consulta_albaran();
                break;
            case 'generar-5':
                consulta_cabecera_albaran();
                break;
            case 'generar-6':
                consulta_oferta_cliente();
                break;
            // Añade casos según sea necesario.
        }
    });
});


function fetchData(url, request) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Destruye la instancia de DataTables si ya existe para evitar errores de re-inicialización
            if ($.fn.DataTable.isDataTable('#data-table')) {
                $('#data-table').DataTable().destroy();
            }

            // Limpia el cuerpo y el encabezado de la tabla antes de añadir nuevos datos
            $('#data-table tbody').empty();
            $('#data-table thead').empty();

            // Si 'titulos' es una cadena en formato JSON, parsearla a un array
            const titulos = JSON.parse(data.titulos);

            // Crea el encabezado de la tabla
            let thead = document.getElementById('data-table').createTHead();
            let headerRow = thead.insertRow();
            titulos.forEach(titulo => {
                let th = document.createElement('th');
                th.textContent = titulo;
                headerRow.appendChild(th);
            });

            // Añade filas de datos al cuerpo de la tabla
            let tbody = document.getElementById('data-table').getElementsByTagName('tbody')[0];
            data.filas.forEach(obj => {
                let newRow = tbody.insertRow();
                Object.keys(obj).forEach(key => {
                    let newCell = newRow.insertCell();
                    let newText = document.createTextNode(obj[key]);
                    newCell.appendChild(newText);
                });
            });


            // Inicializa DataTables
            $('#data-table').DataTable({
                // Configuración de la paginación
                "pagingType": "simple_numbers", // Muestra botones de página y números de página
                "lengthChange": true, // Habilita el menú de selección de cantidad de filas por página
                "searching": true, // Habilita la barra de búsqueda
                "ordering": true, // Habilita la ordenación de columnas
                "info": true, // Muestra información sobre la paginación
                "autoWidth": false, // Deshabilita el ajuste automático del ancho de columnas

                // Configuración para hacer la tabla responsive
                "responsive": {
                    details: {
                        // Definición de cómo se mostrarán los detalles de cada fila en el modo responsive
                        renderer: function (api, rowIdx, columns) {
                            // Se recorren las columnas de la fila actual
                            var data = $.map(columns, function (col, i) {
                                // Si la columna está oculta, se muestra en los detalles
                                return col.hidden ?
                                    // Se crea una fila para mostrar el título y el valor de la columna
                                    '<tr data-dt-row="' + col.rowIndex + '" data-dt-column="' + col.columnIndex + '">' +
                                    '<td>' + col.title + ':' + '</td> ' +
                                    '<td>' + col.data + '</td>' +
                                    '</tr>' :
                                    ''; // Si la columna no está oculta, no se muestra en los detalles
                            }).join(''); // Se unen todas las filas creadas

                            // Si hay datos para mostrar en los detalles, se crea una tabla con ellos
                            return data ?
                                $('<table class="table"/>').append('<tbody>' + data + '</tbody>') :
                                false; // Si no hay datos, se devuelve false
                        }
                    }
                },


                // Configuración para el desplazamiento horizontal y vertical
                "scrollX": true, // Habilita el desplazamiento horizontal
                "scrollY": true, // Habilita el desplazamiento vertical

                // Configuración del lenguaje utilizado en la tabla
                "language": {
                    "search": "Buscar", // Texto para la barra de búsqueda
                    "info": "Se han encontrado _TOTAL_ resultados", // Texto informativo de la paginación
                    "lengthMenu": " Filas: _MENU_", // Menú de selección de cantidad de filas por página
                    "paginate": {
                        "previous": "Anterior", // Texto del botón para página anterior
                        "next": "Siguiente", // Texto del botón para página siguiente
                    }
                }


            }).off('click').on('click', 'tbody tr', function extraer_datos() {

                var dataArray = [];
                $(this).find('td').each(function () { // Itera sobre cada celda de la fila
                    dataArray.push($(this).text()); // Añade el texto de cada celda al array
                });

                console.log(dataArray); // Esto mostrará un array donde cada elemento es el texto de una celda
                console.log(dataArray[2]); // Esto imprimirá el texto de la primera celda

                var cellData = dataArray[2]

                // console.log(thName); // Muestra el valor de la celda en la consola
                var thName = $('#data-table thead th').eq(2).text();

                sendCellDataToBackend(cellData, thName)


                var rowData = $(this).find('td').map(function () {
                    return $(this).text();  // Captura el texto de cada celda en la fila
                }).get();  // Convierte el resultado en un array

                llenarModal();  // Llama a llenarModal con los datos de la fila

            });

        });
}

function llenarModal() {
    $.ajax({
        url: '/get_data_modal/',  // Asegúrate de que esta URL es la correcta
        type: 'GET',
        dataType: 'json',  // Esperamos una respuesta JSON
        success: function(response) {
            if (response.status === 'success') {
                var $tbody = $('#modalTable tbody');
                $tbody.empty();  // Limpia el cuerpo de la tabla modal antes de añadir nuevos datos
                console.log(hola)
                console.log(response)
                console.log(adios)
                response.rows.forEach((row, index) => {
                    var $tr = $('<tr>');  // Crea una nueva fila
                    Object.keys(row).forEach(key => {
                        var $td = $('<td>').text(row[key]);  // Crea una celda con el texto de cada dato
                        $tr.append($td);  // Añade la celda a la fila
                    });
                    $tbody.append($tr);  // Añade la fila al cuerpo de la tabla del modal
                });

                $('#exampleModal').modal('show');  // Muestra el modal
            } else {
                console.log(hola)
                console.log(response)
                console.log(adios)
                console.error('Error:', response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la petición:', error);
        }
    });
}
function sendCellDataToBackend(cellData, columnName) {
    var csrfToken = getCookie('csrftoken'); // Obtener el token CSRF de las cookies

    var dataToSend = JSON.stringify({ cellData: cellData, columName: columnName });
    console.log("Datos a enviar:", dataToSend);  // Esto te ayudará a ver qué se está enviando

    $.ajax({
        url: '/get_data_frontend/',  // Asegúrate de que esta URL es la correcta
        type: 'POST',
        contentType: 'application/json',  // Esto establece que el contenido es JSON
        data: dataToSend,  // Envía los datos como un string JSON
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);  // Esto establece el header CSRFToken necesario para Django
        },
        success: function(response) {
            console.log('Datos enviados correctamente');
        },
    });
}


// Definimos una función llamada getCookie que toma un parámetro 'name'.
// Este 'name' es el nombre de la cookie que queremos buscar.
function getCookie(name) {
    // Inicializamos 'cookieValue' con null. Esto es lo que devolverá la función si no se encuentra la cookie.
    let cookieValue = null;

    // Verificamos si hay alguna cookie almacenada (document.cookie contiene todas las cookies) y si no está vacía.
    if (document.cookie && document.cookie !== '') {
        // Dividimos todas las cookies almacenadas en un array llamado 'cookies'. Cada cookie es un par de clave=valor.
        const cookies = document.cookie.split(';');

        // Recorremos el array de cookies para encontrar la que buscamos.
        for (let i = 0; i < cookies.length; i++) {
            // Eliminamos espacios en blanco al inicio y final de cada cookie y la guardamos en 'cookie'.
            const cookie = cookies[i].trim();

            // Verificamos si el nombre de la cookie actual coincide con el 'name' que estamos buscando.
            // Para ello, comparamos el comienzo de la cadena 'cookie' con el 'name' seguido de un signo igual.
            // Esto es porque las cookies se almacenan como "nombre=valor".
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                // Si encontramos la cookie, decodificamos su valor (por si contiene caracteres especiales)
                // y lo almacenamos en 'cookieValue'. Usamos 'substring' para obtener solo el valor, omitiendo el nombre de la cookie y el signo igual.
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break; // Salimos del bucle porque ya encontramos la cookie que buscábamos.
            }
        }
    }
    // Devolvemos el valor de la cookie encontrada, o null si no se encontró.
    return cookieValue;
}

// Definiciones de funciones de consulta
function consulta1() {
    fetchData('/get_data');
}

function consulta_articulos_precio() {
    fetchData('/get_data_consulta_articulos_precio');
}

function consulta_articulos() {
    fetchData('/get_data_consulta_articulos');
}

function consulta_albaran() {
    fetchData('/get_data_consulta_albaran');
}

function consulta_cabecera_albaran() {
    fetchData('/get_data_consulta_cabecera_albaran');
}
function consulta_oferta_cliente() {
    fetchData('/get_data_oferta_cliente');
}
