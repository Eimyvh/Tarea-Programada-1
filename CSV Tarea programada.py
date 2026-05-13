import csv
def generarCSV(conteo):
    """
    Funcionamiento:
    Esta funcion se encarga de genera un archivo CSV con la información de los reemplazos que se hicieron
    Entradas:
    -conteo: diccionario (diccionario). Contiene las palabras originales, el token asociado y la cantidad de reemplazos.
    Salidas:
    -archivo: archivo CSV (file). Archivo llamado "reporteReemplazos.csv" que contiene los datos de los reemplazos
    """
    archivo = open("reporteReemplazos.csv", "w", newline="", encoding="utf-8") #Crea el archivo 
    writer = csv.writer(archivo)#Writer permite que se pueda escribir en el archivo
    writer.writerow(["Palabra Original", "Token", "Cantidad"]) #Encabezados de las columnas
    for palabra in conteo:
        token = conteo[palabra]["token"] #Esta variable se encarga de obtener el token
        cantidad = conteo[palabra]["cantidad"]#Esta variable se encarga de obtener la cantidad de reemplazos
        writer.writerow([palabra, token, cantidad]) #escribe una fila dentro del csv
    archivo.close() #Este close lo que hace es cerrar el archivo para poder guardarlo bien
tokens = [              #es la listab de los tokens
    ("def", "[FUNCION]"),
    ("return", "[RETORNAR]"),
    ("print", "[PRINT]")]
conteo = {              #es el diccionario para el conteo
    "def":{"token":"[FUNCION]", "cantidad":2},
    "return":{"token": "[RETORNAR]", "cantidad":1},
    "print":{"token": "[IMPRIMIR]", "cantidad":3}
}
generarCSV(conteo)
