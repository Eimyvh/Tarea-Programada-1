def cargarArchivos (pArchivo, pSeparador, pTokensActuales):       
    archivo=open(pArchivo, "r" )
    reemplazados=[]  
    for linea in archivo: #Recorre cada linea.
        linea=linea.strip()
        partes=linea.split(pSeparador) #Separa con el separador que haya ingresado el usuario.
        token=partes[0]
        traduccion=partes[1]
        encontrado=False 
        for i in range(len(pTokensActuales)): #Recorre la lista de tokens usando índices.
            if pTokensActuales[i][0]==token: #Compara el token actual con el que está en el archivo.
                if pTokensActuales[i][1]!=traduccion: #Si la traducción del token es diferente al actual, se reemplaza.
                    pTokensActuales[i]=(token,traduccion)
                    reemplazados.append(token)
                encontrado=True #Indica que el token ya existe en la lista de tokens (ya hubo reemplazo).
        if not encontrado:
            pTokensActuales.append([token,traduccion])
    archivo.close()
    return pTokensActuales,reemplazados

def validarLinea(linea, separador):
    linea=linea.strip()    
    if linea=="":
        return True,None  #Si la linea está vacía se ignora    
    if separador not in linea: 
        return False,"El separador ingresado no se encuentra en el archivo."    
    partes=linea.split(separador, 1) #Divide solo una vez.   
    if len(partes)<2:
        return False, "Debe haber al menos un token y su valor."   
    token=partes[0].strip()
    valor=partes[1].strip()    
    if token=="" or valor=="":
        return False,"Los campos de las lineas se encuentran vacíos."    
    return True, None

def validarArchivo(pArchivo, pSeparador):
    try:
        archivo=open(pArchivo, "r")
        hayDatos=False #Verifica que el archivo tenga al menos una linea válida.       
        for linea in archivo:
            valido,mensaje=validarLinea(linea,pSeparador) #Valida la linea.                   
            if linea.strip()!="":
                hayDatos=True                   
            if not valido:
                archivo.close()
                return False,mensaje              
        if not hayDatos:
            archivo.close() 
            return False,"El archivo está vacío, no contiene ningun token."                
        archivo.close() 
        return True,None #Todo salió bien, None= Ningun mensaje que dar al usuario
    except FileNotFoundError: #Si el archivo no existe.
        return False,"El archivo no existe."

def mostrarTokens (pTokensActuales):
    if pTokensActuales==[]: 
          return []
    resultado=[] #Lista donde se hará el "pretty print".
    for token, traduccion in pTokensActuales: #Recorre los pares de la lista de los tokens actuales.
        resultado.append(f"{token} --> {traduccion}") #Convierte cada tupla en un string más lindo y que sea más fácil de leer.
    return resultado 

def agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales):
    partes=pCadena.split(pSeparadorTokens) #Separa la cadena por el separador que ingresó el usuario.
    agregados=[]
    modificados=[]
    for parte in partes:
        valido,mensaje=validarLinea(parte, pSepararCadena)        
        if not valido:
            print(mensaje)
            continue
        token,valor=parte.split(pSepararCadena, 1) #El 1 es para que solo se divida una vez.
        token=token.strip()
        valor=valor.strip()
        encontrado=False
        for i in range(len(pTokensActuales)):
            if pTokensActuales[i][0]==token:
                pTokensActuales[i]=(token, valor) #Se cambia el token viejo por el nuevo
                modificados.append(token)
                encontrado=True
                break
        if not encontrado:
            pTokensActuales.append((token, valor)) #si no se encuentra aún, agrega.
            agregados.append(token)
    return pTokensActuales, agregados, modificados

def guardarTokensEnArchivo (pArchivoN,pSeparadorInterno,pTokensActuales):
        archivoN=open(pArchivoN, "w") #Aquí se crea el archivo
        for i in range(len(pTokensActuales)):
            token=pTokensActuales[i][0]
            valor=pTokensActuales[i][1]
            linea=token+pSeparadorInterno+valor #se agrega la cadena con el separador que el usuario ingresó.
            if i<len(pTokensActuales) -1: #En todos menos el último
                archivoN.write(linea+"\n") #se juntan todas las cadenas con un salto de linea.
            else:
                archivoN.write(linea)        
        archivoN.close()

def traducirArchivo(pArchivoATraducir, pArchivoNuevo, pTokensActuales):
    import re
    try:
        archivoATraducir=open(pArchivoATraducir, "r")
        archivoNuevo=open(pArchivoNuevo, "w")
        patron=r'"[^"]*"|\'[^\']*\'|[a-zA-Z_]\w*|\s+|[^\w\s]' #ER que separa la línea en strings, tokens, espacios, simbolos.
        for linea in archivoATraducir:
            partes=re.findall(patron, linea) 
            lineaNueva=""
            for parte in partes:
                reemplazada=parte
                if not parte.isspace(): #Evita los espacios.
                    for token in pTokensActuales:
                        if parte==token[0]:
                            reemplazada=token[1]
                lineaNueva+=reemplazada
            archivoNuevo.write(lineaNueva)
        archivoATraducir.close()
        archivoNuevo.close()
    except FileNotFoundError:
        return "El archivo no existe."
    
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
