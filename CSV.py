import csv 
def generarCSV(conteo):
    archivo=open("reporteRemplazo.csv", "escribir",newline="",encoding="utf-8")#El utf es para guardar simbolos como la "Ñ,ñ" y tildes
    escribir=csv.writer(archivo)#Esta varible lo que hace es poder escribir filas en el archivo CSV
    escribir.writerow(["Palabra Original", "Token", "Cantidad"])#Escribe la primera fila del archivo
    for palabra in conteo: #Lo que hace este for es pasar por cada palabra
        token=conteo [palabra]["Token"]#Obtiene el token que este asociado a la palabra 
        cantidad=conteo[palabra]["Cantidad"]#obtiene la cantidad de veces que la palabra digitada fue remplazada
        escribir.writerow([palabra,token,cantidad])#writerow lo que hace es escribir una fila en el CSV con los datos 
    archivo.close()#Este close lo que hace es cerrar el archivo para poder guardarlo bien
    tokens=[("def","[funcion]"), ("return", "[return]"), ("suma", "[variable]")]
