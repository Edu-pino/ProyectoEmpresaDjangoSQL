function consulta1() {
    fetch('/get_data')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';  // Limpia el cuerpo de la tabla antes de añadir nuevos datos
        // Si 'titulos' es una cadena en formato JSON, parsear a un array
        const titulos = JSON.parse(data.titulos);

        // Crear fila de encabezado para títulos
        const headerRow = tableBody.insertRow();
        titulos.forEach(titulo => {
            const headerCell = document.createElement('th');
            headerCell.textContent = titulo;
            headerRow.appendChild(headerCell);
        });
        console.log(data.filas)

        
        // Añadir filas de datos
        data.filas.forEach(rowArray => {
            const newRow = tableBody.insertRow();
            rowArray.forEach(value => {
                const newCell = newRow.insertCell();
                const newText = document.createTextNode(value);
                newCell.appendChild(newText);
            });
        });
    });
}
