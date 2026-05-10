import datetime
def generarHTML(titulo):
    # Obtiene la fecha y hora actual
    fechaHora = datetime.datetime.now()
    # Formato para mostrar fecha y hora dentro del HTML
    fechaMostrar = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
    # Formato para nombre del archivo
    nombreArchivo = fechaHora.strftime("reporteHTML-%d-%m-%y-%H-%M-%S.html")
    # Crea el archivo HTML
    archivoHTML = open(nombreArchivo, "w", encoding="utf-8")
    archivoHTML.write(f"""
<!DOCTYPE html>
<html>

<head>

    <title>{titulo}</title>

</head>

<body>

    <h1>Reporte de Traducción</h1>

    <h2>Fecha y hora de generación: {fechaMostrar}</h2>

</body>

</html>
""")
  
    archivoHTML.close()
    
generarHTML("Reporte TP1")
