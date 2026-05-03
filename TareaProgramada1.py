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

     