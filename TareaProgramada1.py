def cargarArchivos (pArchivo, pSeparador, pTokensActuales):    
    try:
            archivo=open(pArchivo, "r" )
            reemplazados=[]  
            for linea in archivo: #Recorre cada linea.
                linea=linea.strip() 
                partes=linea.split(pSeparador) #Separa con el separador que haya ingresado el usuario.
                token = partes[0]
                traduccion = partes[1]
                encontrado = False 
                for i in range(len(pTokensActuales)):
                    if pTokensActuales[i][0] == token:
                        if pTokensActuales[i][1] != traduccion: #Si la traducción del token es diferente al actual, se reemplaza.
                            pTokensActuales[i] = (token, traduccion)
                            reemplazados.append(token) 
                        encontrado = True #Indica que el token ya existe en la lista de tokens (ya hubo reemplazo).
                if encontrado == False:
                    pTokensActuales.append((token, traduccion))              
            archivo.close()
            return pTokensActuales, reemplazados       
    except FileNotFoundError: #En caso de que no exista el archivo.
        return None
    
import csv 
def generarCSV(conteo):
    archivo=open("reporteRemplazo.csv", "escribir",newline="",encoding="utf-8")#El utf es para guardar simbolos como la "Ñ,ñ" y tildes
    escribir=csv.writer(archivo)
    escribir.writerow(["Palabra Original", "Token", "Cantidad"])
    for palabra in conteo:
        token=conteo [palabra]["Token"]
        cantidad=conteo[palabra]["Cantidad"]
        escribir.writerow([palabra,token,cantidad])
    archivo.close()
    tokens=[("def","[funcion]"), ("return", "[return]"), ("suma", "[variable]")]

     