def archivoExiste(nombre):
    """""
    Funcionamiento: Verifica que el archivo exista y si no devuelve retroalimentación.
    Entradas: nombre -Explicación: Es el nombre del archivo.
    Salidas: 
    True o False (Tipo: Booleano) -Explicación: Identifica si el archivo existe o no (True si sí y False si no).
    None o mensaje (Tipo: String) -Explicación: Retroalimenta al usuario en caso de que no exista o solo se omite el mensaje (None).
    """""
    try:
        archivo = open(nombre, "r")
        archivo.close()
        return True, None
    except FileNotFoundError:
        return False, "El archivo no existe."
    
def validarLinea(linea, separador):
    """""
    Funcionamiento: Valida en las lineas lo siguiente: que no esté vacía (se ignora), que el separador ingresado esté en el archivo, que haya algún token en el archivo,
    que los tokens tengan un valor o que los valores estén asociados a un token.
    Entradas:
    linea -Explicación: Es la linea que se estará revisando.
    separador -Explicación: Separador que se indicó que debería de estár en cada linea.
    Salidas: 
    True (Tipo: Booleano) -Explicación: Indica si todas las líneas cumplen con el formato correcto.
    False (Tipo: Booleano) -Explicación: Indica que el archivo tiene líneas vacías, o que el separador no está en el archivo.
    None o mensaje (Tipo: NoneType, String) -Explicación: Retroalimenta al usuario en caso de que exista la complicación o solo se omite el mensaje (None).
    """""
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

def cargarArchivos (pArchivo, pSeparador, pTokensActuales, bitacora): 
    """""
    Funcionamiento: Guarda los tokens que están almacenados en un archivo ingresado.
    Entradas: 
    pArchivo -Explicación: Es el archivo ingresado.
    pSeparador -Explicación: Es el separador que el usuario menciona que se encuentra separando los tokens dentro del archivo.
    pTokensActuales -Explicación: Es en donde se almacenarán los tokens que se encuentren en el archivo.
    Salidas: 
    pTokensActuales (Tipo: Lista  de tuplas) -Explicación: Son los tokens que se almacenaron.
    reemplazados (Tipo: Lista) -Explicación: Almacena en una lista los tokens que se reemplazaron.
    lineasIncorrectas (Tipo: Lista) -Explicación: Almacena en una lista las que no cumplen con el formato correcto.
    None (Tipo: NoneType) -Explicación: Se utiliza como espacio para imprimir un mensaje en caso de que se haga uso de las validaciones, o se omite el mensaje (None).
    """""      
    valido, mensaje = archivoExiste(pArchivo)
    if not valido:
        registrarAccion(bitacora,"Intentó cargar un archivo inexistente: " + pArchivo,"bitacora.txt")
        return [], [],[],mensaje
    archivo=open(pArchivo, "r" )    
    reemplazados=[]
    lineasIncorrectas=[]  
    for linea in archivo: #Recorre cada linea.
        linea=linea.strip()
        partes=linea.split(pSeparador) #Separa con el separador que haya ingresado el usuario.
        if len(partes)!=2:
            lineasIncorrectas.append(linea)
            registrarAccion(bitacora,"Línea incorrecta ignorada: " + linea,"bitacora.txt")
            continue
        token=partes[0]
        traduccion=partes[1]
        encontrado=False 
        for i in range(len(pTokensActuales)): #Recorre la lista de tokens usando índices.
            if pTokensActuales[i][0]==token: #Compara el token actual con el que está en el archivo.
                if pTokensActuales[i][1]!=traduccion: #Si la traducción del token es diferente al actual, se reemplaza.
                    pTokensActuales[i]=(token,traduccion)
                    reemplazados.append(token)
                    registrarAccion(bitacora, "Token reemplazado: " + token, "bitacora.txt")

                encontrado=True #Indica que el token ya existe en la lista de tokens (ya hubo reemplazo).
        if not encontrado:
            pTokensActuales.append((token,traduccion))
            registrarAccion(bitacora,"Nuevo token agregado: " + token, "bitacora.txt")
    archivo.close()
    registrarAccion(bitacora, "Finalizó carga del archivo: " + pArchivo, "bitacora.txt")
    return pTokensActuales,reemplazados, lineasIncorrectas, None

def validarArchivo(pArchivo, pSeparador):
    """
    Funcionamiento: Valida que el archivo ingresado contenga líneas con el formato correcto y que no esté vacío.
    Entradas: 
    pArchivo -Explicación: Es el archivo que se desea validar.
    pSeparador -Explicación: Es el separador que debe existir entre el token y su traducción dentro de cada línea del archivo.
    Salidas: 
    True (Tipo: Booleano) -Explicación: Indica que el archivo es válido y todas las líneas cumplen con el formato correcto.
    False (Tipo: Booleano) -Explicación: Indica que el archivo tiene líneas inválidas o que está vacío.
    mensaje (Tipo: String) -Explicación: Contiene el mensaje de retroalimentación para cuando el archivo no sea válido.
    None (Tipo: NoneType) -Explicación: Se utiliza cuando no hay mensajes de retroalimentación porque la validación fue correcta.
    """
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
    
def mostrarTokens (pTokensActuales,bitacora):
    """
    Funcionamiento: Convierte la lista de tokens y traducciones en un formato más legible para mostrar al usuario (pretty print).
    Entradas: 
    pTokensActuales -Explicación: Es la lista que contiene los tokens y sus traducciones.
    Salidas: 
    resultado (Tipo: Lista) -Explicación: Almacena los tokens y traducciones convertidos en strings en un pretty print.
    [] (Tipo: Lista) -Explicación: Se retorna una lista vacía cuando no existen tokens almacenados anteriormente.
    """
    if pTokensActuales==[]: 
          registrarAccion(bitacora,"La función mostrarTokens recibió una lista vacía.","bitacora.txt")
          return []
    resultado=[] #Lista donde se hará el "pretty print".
    for token, traduccion in pTokensActuales: #Recorre los pares de la lista de los tokens actuales.
        resultado.append(f"{token} --> {traduccion}") #Convierte cada tupla en un string más lindo y que sea más fácil de leer.
    registrarAccion(bitacora,f"Se procesaron {len(pTokensActuales)} tokens para mostrarlos.","bitacora.txt")
    return resultado 

def agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales,bitacora):
    """
    Funcionamiento: Agrega nuevos tokens o modifica los que ya estén almacenados mediante una cadena que ingrese el usuario.
    Entradas: 
    pCadena -Explicación: Es la cadena que contiene los tokens y traducciones que se desean agregar o modificar.
    pSeparadorTokens -Explicación: Es el separador utilizado para dividir cada token dentro de la cadena.
    pSepararCadena -Explicación: Es el separador utilizado entre el token y su traducción.
    pTokensActuales -Explicación: Es la lista donde se almacenan los tokens actuales.
    Salidas: 
    pTokensActuales (Tipo: Lista de tuplas) -Explicación: Tiene los tokens actualizados después de agregar o modificar alguno.
    agregados (Tipo: Lista) -Explicación: Almacena los tokens que fueron agregados por primera vez.
    modificados (Tipo: Lista) -Explicación: Almacena los tokens que ya existían y fueron modificados.
    """
    partes=pCadena.split(pSeparadorTokens) #Separa la cadena por el separador que ingresó el usuario.
    agregados=[]
    modificados=[]
    for parte in partes:
        valido,mensaje=validarLinea(parte, pSepararCadena)        
        if not valido:
            registrarAccion(bitacora,f"Línea inválida detectada: '{parte}'. Motivo: {mensaje}","bitacora.txt")

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
                registrarAccion(bitacora,f"Se modificó el token '{token}'.","bitacora.txt")
                encontrado=True
                break
        if not encontrado:
            pTokensActuales.append((token, valor)) #si no se encuentra aún, agrega.
            agregados.append(token)
            registrarAccion(bitacora,f"Se agregó el token '{token}'.","bitacora.txt")
    return pTokensActuales, agregados, modificados

def guardarTokensEnArchivo (pArchivoN,pSeparadorInterno,pTokensActuales,bitacora):
        """
        Funcionamiento: Guarda en un archivo los tokens y traducciones almacenados en la lista de tokens actuales.
        Entradas: 
        pArchivoN -Explicación: Es el nombre del archivo donde se guardarán los tokens almacenados.
        pSeparadorInterno -Explicación: Es el separador que se colocará entre el token y su traducción dentro del archivo.
        pTokensActuales -Explicación: Es la lista que tiene los tokens y traducciones que se desean guardar.
        Salidas: 
        Ninguna salida -Explicación: La función únicamente guarda información en el archivo.
        """
        if pTokensActuales==[]:
            registrarAccion(bitacora,"Se intentó guardar tokens pero la lista estaba vacía.","bitacora.txt")
            return
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
        registrarAccion(bitacora,f"Se guardaron {len(pTokensActuales)} tokens en el archivo '{pArchivoN}'.","bitacora.txt")
    
def traducirArchivo(pArchivoATraducir, pArchivoNuevo, pTokensActuales, bitacora):
    """
    Funcionamiento: Traduce el contenido de un archivo utilizando los tokens almacenados y guarda el resultado en un nuevo archivo.
    Entradas: 
    pArchivoATraducir -Explicación: Es el archivo que tiene el código o texto que se desea traducir.
    pArchivoNuevo -Explicación: Es el nombre del archivo donde se guardará el contenido ya traducido.
    pTokensActuales -Explicación: Es la lista que contiene los tokens y sus traducciones.
    bitacora -Explicación: Es la lista  donde se registran las acciones realizadas durante la traducción.
    Salidas: 
    Ninguna salida -Explicación: La función realiza la traducción y guarda el resultado en un archivo, pero no retorna nada.
    """
    import re
    archivoATraducir=open(pArchivoATraducir, "r")
    archivoNuevo=open(pArchivoNuevo, "w")
    patron=r'"[^"]*"|\'[^\']*\'|[a-zA-Z_]\w*|\s+|[^\w\s]' #ER que separa la línea en strings, tokens, espacios, simbolos.
    reemplazados=0
    for linea in archivoATraducir:
        partes=re.findall(patron, linea) 
        lineaNueva=""
        for parte in partes:
            reemplazada=parte
            if not parte.isspace(): #Evita los espacios.
                for token in pTokensActuales:
                    if parte==token[0]:
                        reemplazada=token[1]
                        reemplazados+=1
                        registrarAccion(bitacora, f"Se hizo el reemplazo de : {token[0]} → {token[1]}", "bitacora.txt")
            lineaNueva+=reemplazada
        archivoNuevo.write(lineaNueva)
    archivoATraducir.close()
    archivoNuevo.close()
    registrarAccion(bitacora,f"Traducción completada con {reemplazados} reemplazos realizados.","bitacora.txt")
