import datetime

def generarReporteHTML(titulo, duracion, totalReemplazos, porcentaje, listaTokens):
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
    archivoHTML = open(nombreArchivo, "w", encoding="utf-8")#Abrir archivo HTML en modo escritura
    # Este f""" sirve para escribir muchas líneas seguidas  y meter variables dentro del texto
    archivoHTML.write(f"""
<!DOCTYPE html>
<html>
<head>

    <meta charset="UTF-8">

    <!-- Título de la pestaña -->
    <title>{titulo}</title>

    <style>

        body{{
            front-family:Times New Roman
            margin:30px;
            background-color: white;
            color: black;
        }}
        h1{{
            text-align center;
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