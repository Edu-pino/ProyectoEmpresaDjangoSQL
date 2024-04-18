import pyodbc
import json
from django.shortcuts import render

class Connection:
    
    def obtener_nombres_columnas(cursor):
        column_info = cursor.description
        column_names = [column[0] for column in column_info]
        column_names_json = json.dumps(column_names)
        return column_names_json
    
    def delvolver_filas_columnas(rows,colum):
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
    
    def conexion():
        server = 'SSAGE01'
        database = 'LogicClass'
        username = 'bigdata'
        password = 'Sistemas2005.'

        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            print("¡Conexión exitosa!")
            return conn
        except pyodbc.Error as err:
            print("Error al conectarse a la base de datos: {}".format(err))
            
            
    def consulta_1 (request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT CabeceraAlbaranCliente.RazonSocial, MovimientoArticuloSerie.NumeroSerieLc,CASE WHEN (CabeceraAlbaranCliente.ImporteCambio <> 0) THEN -1 ELSE 0 END AS ImprimirIvaEnDivisa_, LineasAlbaranCliente.EjercicioAlbaran, LineasAlbaranCliente.SerieAlbaran, LineasAlbaranCliente.NumeroAlbaran, LineasAlbaranCliente.Orden, LineasAlbaranCliente.FechaRegistro, LineasAlbaranCliente.FechaAlbaran, LineasAlbaranCliente.LineasPosicion, LineasAlbaranCliente.CodigoArticulo, LineasAlbaranCliente.CodigoAlmacen, LineasAlbaranCliente.Partida, LineasAlbaranCliente.DescripcionArticulo, LineasAlbaranCliente.Descripcion2Articulo, LineasAlbaranCliente.DescripcionLinea, LineasAlbaranCliente.NumeroAgrupaciones, LineasAlbaranCliente.UnidadesAgrupacion, LineasAlbaranCliente.Unidades, LineasAlbaranCliente.Precio, LineasAlbaranCliente.ImporteBruto, LineasAlbaranCliente.[%Descuento], LineasAlbaranCliente.ImporteDescuento, LineasAlbaranCliente.ImporteNeto, LineasAlbaranCliente.[%Iva], LineasAlbaranCliente.[%Recargo], LineasAlbaranCliente.ImporteLiquido, LineasAlbaranCliente.UnidadMedida1_, LineasAlbaranCliente.UnidadMedida2_, LineasAlbaranCliente.Unidades2_, LineasAlbaranCliente.GrupoTalla_, LineasAlbaranCliente.CodigoColor_, LineasAlbaranCliente.CodigoTalla01_, LineasAlbaranCliente.ImporteBrutoDivisa_, LineasAlbaranCliente.ImporteDescuentoDivisa_, LineasAlbaranCliente.ImporteNetoDivisa_, LineasAlbaranCliente.ImporteLiquidoDivisa_, LineasAlbaranCliente.SuPedido, LineasAlbaranCliente.[%Descuento2], LineasAlbaranCliente.[%Descuento3], LineasAlbaranCliente.CodigodelCliente, LineasAlbaranCliente.ImporteEnvases_, LineasAlbaranCliente.ImporteEnvasesDivisa_, LineasAlbaranCliente.NumeroEnvases_, LineasAlbaranCliente.NumeroSerieLc, CabeceraAlbaranCliente.PesoBruto_, CabeceraAlbaranCliente.PesoNeto_, CabeceraAlbaranCliente.Volumen_, CabeceraAlbaranCliente.PuertoDestino_, CabeceraAlbaranCliente.PuertoOrigen_, CabeceraAlbaranCliente.ObservacionExportacion_, CabeceraAlbaranCliente.ObservacionExportacion2_, CabeceraAlbaranCliente.ImporteFletes_, CabeceraAlbaranCliente.ImporteFletesDivisa_, CabeceraAlbaranCliente.ImporteSeguro_, CabeceraAlbaranCliente.ImporteSeguroDivisa_, CabeceraAlbaranCliente.GastosAduana_, CabeceraAlbaranCliente.GastosAduanaDivisa_, Transportistas.Transportista, Transportistas.Municipio, Transportistas.Nacion, Transportistas.Provincia, Transportistas.ViaPublica, Transportistas.CodigoPostal, CabeceraAlbaranCliente.IdDelegacion, CabeceraAlbaranCliente.EjercicioAlbaran, CabeceraAlbaranCliente.SerieAlbaran, CabeceraAlbaranCliente.NumeroAlbaran, CabeceraAlbaranCliente.FechaAlbaran, CabeceraAlbaranCliente.CodigoCliente, CabeceraAlbaranCliente.CodigoContable, CabeceraAlbaranCliente.CifEuropeo, CabeceraAlbaranCliente.Nombre, CabeceraAlbaranCliente.RazonSocial, CabeceraAlbaranCliente.Domicilio, CabeceraAlbaranCliente.CodigoPostal, CabeceraAlbaranCliente.CodigoBanco, CabeceraAlbaranCliente.CodigoAgencia, CabeceraAlbaranCliente.DC, CabeceraAlbaranCliente.CCC, CabeceraAlbaranCliente.[%Descuento], CabeceraAlbaranCliente.[%ProntoPago], CabeceraAlbaranCliente.[%Financiacion], CabeceraAlbaranCliente.CodigoComisionista, CabeceraAlbaranCliente.[%Comision], CabeceraAlbaranCliente.CodigoZona, CabeceraAlbaranCliente.CopiasAlbaran, CabeceraAlbaranCliente.ObservacionesCliente, CabeceraAlbaranCliente.ObservacionesAlbaran, CabeceraAlbaranCliente.ObservacionesFactura, CabeceraAlbaranCliente.Bultos, CabeceraAlbaranCliente.ImportePortes, CabeceraAlbaranCliente.EjercicioPedido, CabeceraAlbaranCliente.SeriePedido, CabeceraAlbaranCliente.NumeroPedido, CabeceraAlbaranCliente.ImporteDescuentoLineas, CabeceraAlbaranCliente.ImporteNetoLineas, CabeceraAlbaranCliente.ImporteDescuento, CabeceraAlbaranCliente.ImporteProntoPago, CabeceraAlbaranCliente.BaseImponible, CabeceraAlbaranCliente.ImporteFinanciacion, CabeceraAlbaranCliente.ImporteFactura, CabeceraAlbaranCliente.[%Retencion], CabeceraAlbaranCliente.ImporteRetencion, CabeceraAlbaranCliente.ImporteLiquido, CabeceraAlbaranCliente.NombreEnvios, CabeceraAlbaranCliente.DomicilioEnvios, CabeceraAlbaranCliente.CodigoPostalEnvios, CabeceraAlbaranCliente.CodigoMunicipioEnvios, CabeceraAlbaranCliente.ColaMunicipioEnvios, CabeceraAlbaranCliente.CodigoProvinciaEnvios, CabeceraAlbaranCliente.CodigoNacionEnvios, CabeceraAlbaranCliente.TelefonoEnvios, CabeceraAlbaranCliente.FaxEnvios, CabeceraAlbaranCliente.CodigoDivisa, CabeceraAlbaranCliente.ImporteNetoLineasDivisa_, CabeceraAlbaranCliente.ImporteDescuentoDivisa_, CabeceraAlbaranCliente.ImporteProntoPagoDivisa_, CabeceraAlbaranCliente.BaseImponibleDivisa_, CabeceraAlbaranCliente.ImporteFinanciacionDivisa_, CabeceraAlbaranCliente.ImporteFacturaDivisa_, CabeceraAlbaranCliente.ImporteRetencionDivisa_, CabeceraAlbaranCliente.ImporteLiquidoDivisa_, CabeceraAlbaranCliente.ImportePortesDivisa_, CabeceraAlbaranCliente.FormadePago, CabeceraAlbaranCliente.Municipio, CabeceraAlbaranCliente.SuPedido, CabeceraAlbaranCliente.Provincia, CabeceraAlbaranCliente.Nacion, CabeceraAlbaranCliente.MunicipioEnvios, CabeceraAlbaranCliente.ProvinciaEnvios, CabeceraAlbaranCliente.NacionEnvios, CabeceraAlbaranCliente.RazonSocialEnvios, CabeceraAlbaranCliente.[%Rappel], CabeceraAlbaranCliente.RazonSocial2, CabeceraAlbaranCliente.Domicilio2, CabeceraAlbaranCliente.RazonSocial2Envios, CabeceraAlbaranCliente.Domicilio2Envios, CabeceraAlbaranCliente.ImporteRappel, CabeceraAlbaranCliente.AlbaranValorado, CabeceraAlbaranCliente.CodigoTransportistaEnvios, CabeceraAlbaranCliente.TipoPortesEnvios, CabeceraAlbaranCliente.ImporteRappelDivisa_, CabeceraAlbaranCliente.ViaPublicaEnvios, CabeceraAlbaranCliente.CodigoRuta_, CabeceraAlbaranCliente.IvaIncluido, CabeceraAlbaranCliente.EnEuros_, CabeceraAlbaranCliente.ImporteEnvases_, CabeceraAlbaranCliente.ImporteEnvasesDivisa_, CabeceraAlbaranCliente.ImporteCambio, CabeceraAlbaranCliente.GenerarFactura, CabeceraAlbaranCliente.ImporteACuentaA_, CabeceraAlbaranCliente.ImporteACuentaADivisa_, LineasAlbaranCliente.Lote_, LineasAlbaranCliente.Componente FROM CabeceraAlbaranCliente WITH (NOLOCK) LEFT OUTER JOIN LineasAlbaranCliente WITH (NOLOCK) ON CabeceraAlbaranCliente.CodigoEmpresa = LineasAlbaranCliente.CodigoEmpresa AND CabeceraAlbaranCliente.EjercicioAlbaran = LineasAlbaranCliente.EjercicioAlbaran AND CabeceraAlbaranCliente.SerieAlbaran = LineasAlbaranCliente.SerieAlbaran AND CabeceraAlbaranCliente.NumeroAlbaran = LineasAlbaranCliente.NumeroAlbaran LEFT OUTER JOIN CabeceraAlbaranClienteCola_ WITH (NOLOCK) ON CabeceraAlbaranCliente.CodigoEmpresa = CabeceraAlbaranClienteCola_.CodigoEmpresa AND CabeceraAlbaranCliente.EjercicioAlbaran = CabeceraAlbaranClienteCola_.EjercicioAlbaran AND CabeceraAlbaranCliente.SerieAlbaran = CabeceraAlbaranClienteCola_.SerieAlbaran AND CabeceraAlbaranCliente.NumeroAlbaran = CabeceraAlbaranClienteCola_.NumeroAlbaran LEFT OUTER JOIN Transportistas WITH (NOLOCK) ON CabeceraAlbaranCliente.CodigoEmpresa = Transportistas.CodigoEmpresa AND CabeceraAlbaranCliente.CodigoTransportistaEnvios = Transportistas.CodigoTransportista LEFT OUTER JOIN MovimientoArticuloSerie WITH (NOLOCK) ON MovimientoArticuloSerie.CodigoEmpresa = LineasAlbaranCliente.CodigoEmpresa AND MovimientoArticuloSerie.EjercicioDocumento = LineasAlbaranCliente.EjercicioAlbaran AND MovimientoArticuloSerie.SerieDocumento = LineasAlbaranCliente.SerieAlbaran AND MovimientoArticuloSerie.Documento = LineasAlbaranCliente.NumeroAlbaran AND MovimientoArticuloSerie.MovPosicionOrigen = LineasAlbaranCliente.LineasPosicion WHERE CabeceraAlbaranCliente.CodigoCliente = '{}'  ORDER BY CabeceraAlbaranCliente.CodigoEmpresa, CabeceraAlbaranCliente.EjercicioAlbaran, CabeceraAlbaranCliente.SerieAlbaran, CabeceraAlbaranCliente.NumeroAlbaran, LineasAlbaranCliente.Orden, LineasAlbaranCliente.FechaRegistro, MovimientoArticuloSerie.NumeroSerieLc;".format(codigo_cliente))
        
        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
       
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum)
    


    def consulta_articulos(request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT CodigoEmpresa, CodigoArticulo, DescripcionArticulo, MarcaProducto, CodigoProveedor, CodigoFamilia, CONVERT(VARCHAR,FechaAlta, 105) AS FechaAlta FROM dbo.Articulos WHERE CodigoEmpresa = '1000';")
        
        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum)
    
    def consulta_articulos_precio (request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT CodigoEmpresa, CodigoArticulo, FORMAT(PrecioCompra, 'N2') AS PrecioCompra, FORMAT(PrecioVenta, 'N2') AS PrecioVenta, FORMAT(PrecioVentaconIVA1, 'N2') AS PrecioVentaIVA, FORMAT(PrecioVentasinIVA1, 'N2') AS PrecioVentasinIVA FROM dbo.Articulos WHERE CodigoEmpresa = '1000';")
        
        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum)
    
    
    def consulta_albaran(request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT A.CodigoArticulo , A.DescripcionArticulo , FORMAT(A.Unidades, 'N2') AS Unidades ,FORMAT(A.Precio, 'N2') AS Precio  from dbo.LineasAlbaranCliente AS A INNER JOIN dbo.CabeceraAlbaranCliente AS L ON A.NumeroAlbaran = L.NumeroAlbaran WHERE L.CodigoEmpresa = '1000' AND CodigoCliente = '{}';".format(codigo_cliente))
        
        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum)
    
    def consulta_cabecera_albaran(request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT CA.EjercicioAlbaran , CA.SerieAlbaran, CA.NumeroAlbaran, CONVERT(VARCHAR,CA.FechaAlbaran,105) AS FechaAlbaran, C.CodigoCliente FROM dbo.CabeceraAlbaranCliente AS CA INNER JOIN dbo.Clientes AS C ON CA.RazonSocial = C.RazonSocial WHERE C.CodigoEmpresa = '1000' AND C.CodigoCliente = '{}';".format(codigo_cliente))

        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum) 

    def OfertaCliente(request):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT CO.RazonSocial, CO.NumeroOferta, CONVERT(VARCHAR,CO.FechaOferta,105) AS FECHA_OFERTA, LC.CodigoArticulo, LC.DescripcionArticulo, CO.FormadePago ,  FORMAT(CO.ImporteCoste,'N2') AS IMPORTE_COSTE,FORMAT(CO.ImporteBruto,'N2') AS IMPORTE_BRUTO, FORMAT(CO.TotalIva,'N2') AS TOTAL_IVA, FORMAT(CO.ImporteFactura,'N2') AS IMPORTE_FACTURA,  FORMAT(CO.MargenBeneficio,'N2') AS MARGEN_BENEFICIO, LC.Descripcion2Articulo, LC.DescripcionLinea, LC.CodigoFamilia, LC.CodigoSubfamilia, FORMAT(LC.UnidadesPedidas,'N2') AS UNIDADES_PEDIDAS, FORMAT(LC.UnidadesaServir,'N2') AS UNIDADES_SERVIDAS, FORMAT(LC.Precio,'N2') AS PRECIO, FORMAT(LC.PrecioCoste,'N2') AS PRECIO_COSTE, LC.CodigoIva, LC.TipoArticulo, FORMAT(LC.PorMargenBeneficio,'N2') AS POR_MARGEN_BENEFICIO, FORMAT(LC.MargenBeneficio,'N2') AS MARGEN_BENEFICIO from dbo.CabeceraOfertaCliente AS CO INNER JOIN dbo.LineasOfertaCliente AS LC ON CO.NumeroOferta = LC.NumeroOferta WHERE CO.CodigoEmpresa = '1000' AND CO.CodigoCliente = '{}';".format(codigo_cliente))

        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum) 
    


    
    def table_modal(request):
        print("he entrado en la funcion table modal")
        from app_sage.views import extraercodigocliente , get_data_frontend
        codigo_cliente = extraercodigocliente(request)
        colum = get_data_frontend(request)
        print("he obtenudo el codigo cliente")
        
        # Llamada al método para obtener los datos de la celda y la columna
    
        
        # Realizar la conexión a la base de datos
        conn = Connection.conexion()
        cursor = conn.cursor()
        print("HE hecho la conexion")
        # Ejecutar la consulta utilizando los datos obtenidos
        cursor.execute("SELECT L.CodigoArticulo , L.DescripcionArticulo , L.Unidades , L.Precio , L.ImporteBruto from dbo.LineasAlbaranCliente as L INNER JOIN dbo.CabeceraAlbaranCliente as CO ON CO.NumeroAlbaran = L.NumeroAlbaran WHERE CO.CodigoEmpresa = '1000' AND CO.CodigoCliente = '{}' AND CO.{} = '{}';".format(codigo_cliente , colum[1] , colum[0]))
        
        print("He salido de la query")
        # Obtener nombres de columnas y filas
        
        
        try:
            rows = cursor.fetchall()
            print("Data retrieved:", rows)
        except Exception as e:
            print("Error fetching data:", str(e))
        colum = "hola"
        
        # Cerrar el cursor y la conexión
        conn.close()
        
        # Devolver filas y columnas en el formato adecuado
        return Connection.delvolver_filas_columnas(rows, colum) 


    def LineasAlbaran(request,cell_data, colum_name):
        from app_sage.views import extraercodigocliente # Hacemos la importancion aqui para que el metodo no pete
        codigo_cliente = extraercodigocliente(request)
        conn = Connection.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT L.CodigoArticulo , L.DescripcionArticulo , L.Unidades , L.Precio , L.ImporteBruto from dbo.LineasAlbaranCliente as L INNER JOIN dbo.CabeceraAlbaranCliente as CO ON CO.NumeroAlbaran = L.NumeroAlbaran WHERE CO.CodigoEmpresa = '1000' AND CO.CodigoCliente = '{}' AND {} = '{}';".format(codigo_cliente, colum_name ,cell_data  ))

        colum = Connection.obtener_nombres_columnas(cursor)
        rows = cursor.fetchall()
        print(rows)
        # Cerrar el cursor y la conexión
        conn.close()
        return Connection.delvolver_filas_columnas(rows,colum) 
