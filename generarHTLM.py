
import datetime

def generarReporteHTML(titulo,conteo, duracion, totalReemplazos, porcentaje):
    """
    Funcionamiento: Esta función lo que nos permite hacer es la generacion de un archivo HTML con un reporte de traducción.
    Entrada
    - titulo (str): título que aparecerá en la pestaña del navegador
    - duracion (float): duración total del procesamiento
    - totalReemplazos (int): cantidad total de reemplazos realizados
    - porcentaje (float): porcentaje de palabras reemplazadas
    - listaTokens (list): lista de tuplas con:
        (palabraOriginal (str), reemplazo (str), cantidad (int))
    Salidas:
    - Genera un archivo HTML
    """
    fechaHora = datetime.datetime.now() # el datetime es para obtener la fecha y hora actual
    fechaMostrar = fechaHora.strftime("%d/%m/%Y %H:%M:%S")#Es la fecha que se va a mostrar dentro del HTML
    nombreArchivo = fechaHora.strftime("reporteHTML_%d-%m-%y-%H-%M-%S.html") #Aqui usamos guiones porque "/" y ":" no funcionan e investigando vimos que es por que windows lo puede identificar de otra manera 
    # Abrir archivo HTML en modo escritura
    archivoHTML = open(nombreArchivo, "w", encoding="utf-8")
    # Este f""" sirve para escribir muchas líneas seguidas  y meter variables dentro del texto
    archivoHTML.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <!-- Título de la pestaña -->
    <title>{titulo}</title>
    <style>
        body {{
            font-family: Arial;
            margin: 30px;
            background-color: white;
            color: black;
        }}
        h1 {{
            text-align: center;
            color: black;
        }}
        h2 {{
            text-align: center;
            color: red;
        }}
        p {{
            font-size: 18px;
        }}
        /* Tabla */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        /* Bordes */
        table, th, td {{
            border: 1px solid black;
        }}
        /* Encabezados */
        th {{
            background-color: black;
            color: white;
            padding: 10px;
        }}
        /* Celdas */
        td {{
            padding: 10px;
            text-align: center;
        }}
        /* Filas alternas */
        tr:nth-child(even) {{
            background-color: #e6e6e6;
        }}
        tr:nth-child(odd) {{
            background-color: white;
        }}
    </style>
</head>
<body>
    <h1>Reporte de Traducción</h1>
    <h2>Fecha y hora de generación: {fechaMostrar}</h2>
    <p>Duración total del procesamiento: {duracion} segundos</p>
    <p>Cantidad total de reemplazos: {totalReemplazos}</p>
    <p>Porcentaje de palabras reemplazadas: {porcentaje}%</p>
    <table>
        <tr>
            <th>Palabra Original</th>
            <th>Token</th>
            <th>Cantidad</th>
        </tr>
""")
    for palabra in conteo:
        token = conteo[palabra]["token"]
        cantidad = conteo[palabra]["cantidad"]
        archivoHTML.write(f"""
        <tr>
            <td>{palabra}</td>
            <td>{token}</td>
            <td>{cantidad}</td>
        </tr>
""")
    archivoHTML.write("""
    </table>

</body>
</html>
""")
    archivoHTML.close()#aqui se cierra ya el archivo
conteo = {
    "def": {"token": "[FUNCION]", "cantidad": 2},
    "return": {"token": "[RETORNAR]", "cantidad": 1},
    "print": {"token": "[IMPRIMIR]", "cantidad": 3}
}
# Genera el HTML
generarReporteHTML(
    "Reporte TP1",
    conteo,
    2.5,
    6,
    75
)