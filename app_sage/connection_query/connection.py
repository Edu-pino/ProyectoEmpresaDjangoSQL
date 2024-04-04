import pyodbc
import json

class Connection:
    
    def obtener_nombres_columnas(cursor):
        column_info = cursor.description
        column_names = [column[0] for column in column_info]
        return column_names
    
    
    
    def conexion(request):
        from app_sage.views import extraercodigocliente #Hacemos la importancia aqui para que el metodo no pete

        server = 'SSAGE01'
        database = 'LogicClass'
        username = 'bigdata'
        password = 'Sistemas2005.'

        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            print("¡Conexión exitosa!")
            codigo_cliente = extraercodigocliente(request)

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.Clientes WHERE CodigoEmpresa = '1000' AND CodigoCliente = '{}';".format(codigo_cliente))
            

            colum = Connection.obtener_nombres_columnas(cursor)
            
          
            
            rows = cursor.fetchall()
            # Cerrar el cursor y la conexión
            conn.close()
            all_rows = []
            
            
            #Recorremos todas las filas que nos ha devuelto la consulta
            for row in rows:
                # Iniciamos y reiniciamos el array temporal
                array_temp = {}
                # guardamos la longitud de la fila, es decir, el numero de campos que ha devuelto la consulta
                lenRow = len(row)
                # recorremos la fila
                for i in range(lenRow):
                    # accedemos a cada campo y lo guardamos en el array temporal usando como clave el valor de i
                    array_temp[f"{i}"] = row[i]
                # Añadimos el array a UNA posicion de all_row, asi cada posicion de all_row tendra todos los valores de una fila
                all_rows.append(array_temp)

                
                
                
                
            # Lista para almacenar todas las filas
            return all_rows,colum

        except pyodbc.Error as err:
            print("Error al conectarse a la base de datos: {}".format(err))
            

    
    
