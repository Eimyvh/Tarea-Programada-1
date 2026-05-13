#Elaborado por: Eimy Vega Hidalgo y Zaid Chaves Durán.
#Fecha de creación:26/04/2026
#Ultima modificación:12/05/2026
#Versión: Python 3.14 (64-bit)
"""
Librerías utilizadas en las funciones:
"""
import csv
from datetime import datetime
import pickle

def opcionVacia(variable):
    """
    Funcionamiento: Verifica si una variable se encuentra vacia.
    Entradas:
    - variable: dato que se quiere validar (string).
    Salidas:
    - True: si la variable esta vacia.
    - False: si la variable tiene información.
    """
    if variable == "":
        return True
    return False

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
    except FileNotFoundError: #No se encuentra el archivo.
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
        return False, "Debe haber al menos un token con su respectivo valor."   
    token=partes[0].strip()
    valor=partes[1].strip()    
    if token=="" or valor=="":
        return False,"Los campos en las lineas se encuentran vacíos."    
    return True, None

def cargarArchivos (pArchivo, pSeparador, pTokensActuales, bitacora): 
    """
    Funcionamiento: Carga los tokens almacenados dentro de un archivo, valida su formato y actualiza 
    la lista de tokens actuales. Además, registra las acciones realizadas dentro de la bitácora.
    Entradas: 
    pArchivo -Explicación: Es el nombre del archivo que contiene los tokens y traducciones que se desean cargar.
    pSeparador -Explicación: Es el separador utilizado dentro del archivo para dividir cada token de su traducción.
    pTokensActuales -Explicación: Es la lista donde se almacenan los tokens y traducciones cargados actualmente.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas durante la carga del archivo.
    Salidas: 
    pTokensActuales (Tipo: Lista de tuplas) -Explicación: Contiene los tokens y traducciones actualizados después de cargar el archivo.
    reemplazados (Tipo: Lista) -Explicación: Almacena los tokens que ya existían y fueron reemplazados por nuevos valores.
    lineasIncorrectas (Tipo: Lista) -Explicación: Contiene las líneas que no tenían el formato correcto y no fueron agregadas.
    mensaje (Tipo: String) -Explicación: Devuelve un mensaje de error si el archivo no existe.
    None (Tipo: NoneType) -Explicación: Se retorna cuando el archivo se procesó correctamente y no ocurrió ningún error.
    """     
    valido, mensaje = archivoExiste(pArchivo)
    if not valido:
        registrarAccion(bitacora,"Intentó cargar un archivo que no existía: " + pArchivo,"bitacora.txt") #Para registrar en bitácora.
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
                    registrarAccion(bitacora, "Se reempló el token : " + token, "bitacora.txt")
                encontrado=True #Indica que el token ya existe en la lista de tokens (ya hubo reemplazo).
        if not encontrado:
            pTokensActuales.append((token,traduccion))
            registrarAccion(bitacora,"Nuevo token agregado: " + token, "bitacora.txt")
    archivo.close()
    registrarAccion(bitacora, "Terminó la carga del archivo: " + pArchivo, "bitacora.txt")
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
    hayDatos=False #Bandera qu verifica que el archivo tenga al menos una linea válida.       
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
    return True,None #Todo salió bien, None:Ningun mensaje que dar al usuario.
    
def mostrarTokens (pTokensActuales,bitacora):
    """
    Funcionamiento: Convierte los tokens almacenados en un formato más legible para el usuario 
    y registra en la bitácora las acciones realizadas durante el proceso.
    Entradas: 
    pTokensActuales -Explicación: Es la lista que contiene los tokens y sus respectivas traducciones almacenadas actualmente.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas dentro del programa.
    Salidas: 
    resultado (Tipo: Lista) -Explicación: Contiene los tokens y traducciones convertidos en un formato más fácil de leer para el usuario.
    [] (Tipo: Lista) -Explicación: Se retorna una lista vacía cuando no existen tokens almacenados actualmente.
    """
    if pTokensActuales==[]: 
          registrarAccion(bitacora,"La función mostrarTokens recibió una lista vacía.","bitacora.txt")
          return []
    resultado=[] #Lista donde se hará el "pretty print".
    for token, traduccion in pTokensActuales:
        resultado.append(f"{token} --> {traduccion}") #Convierte cada tupla en un string más lindo y que sea más fácil de leer.
    registrarAccion(bitacora,f"Se procesaron {len(pTokensActuales)} tokens para mostrarlos.","bitacora.txt")
    return resultado 

def agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales,bitacora):
    """
    Funcionamiento: Agrega nuevos tokens o modifica los que ya existen utilizando una cadena ingresada por el usuario.
    Entradas: 
    pCadena -Explicación: Es la cadena que contiene los tokens y sus valores.
    pSeparadorTokens -Explicación: Es el separador que divide cada token dentro de la cadena.
    pSepararCadena -Explicación: Es el separador que divide el token de su valor.
    pTokensActuales -Explicación: Es la lista donde están almacenados los tokens actuales.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas.
    Salidas: 
    pTokensActuales (Tipo: Lista de tuplas) -Explicación: Contiene los tokens actualizados después de agregar o modificar datos.
    agregados (Tipo: Lista) -Explicación: Guarda los tokens que fueron agregados por primera vez.
    modificados (Tipo: Lista) -Explicación: Guarda los tokens que ya existían y fueron modificados.
    """
    partes=pCadena.split(pSeparadorTokens) #Separa la cadena por el separador que ingresó el usuario.
    agregados=[]
    modificados=[]
    for parte in partes:
        valido,mensaje=validarLinea(parte, pSepararCadena)        
        if not valido:
            registrarAccion(bitacora,f"Se detectó una línea inválida: '{parte}'. Motivo: {mensaje}","bitacora.txt")
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
                registrarAccion(bitacora,f"Se modificó el token: '{token}'.","bitacora.txt")
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
        pTokensActuales -Explicación: Es la lista que contiene los tokens y traducciones que se desean guardar.
        bitacora -Explicación: Es la lista donde se registran las acciones realizadas.
        Salidas: 
        Ninguna salida -Explicación: La función únicamente guarda la información en un archivo.
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
    
def traducirArchivo(pArchivoATraducir, pArchivoNuevo, pTokensActuales, bitacora,conteo):
    """
    Funcionamiento: Traduce el contenido de un archivo utilizando los tokens almacenados y guarda el resultado en un nuevo archivo.
    Entradas: 
    pArchivoATraducir -Explicación: Es el archivo que contiene el texto o código que se desea traducir.
    pArchivoNuevo -Explicación: Es el nombre del archivo donde se guardará el contenido traducido.
    pTokensActuales -Explicación: Es la lista que contiene los tokens y sus traducciones.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas durante la traducción.
    conteo -Explicación: Es el diccionario donde se almacenan las estadísticas de reemplazos realizados.
    Salidas: 
    reemplazados (Tipo: Entero) -Explicación: Cantidad total de reemplazos realizados durante la traducción.
    totalPalabras (Tipo: Entero) -Explicación: Cantidad total de palabras o elementos revisados en el archivo.
    """
    import re
    archivoATraducir=open(pArchivoATraducir, "r")
    archivoNuevo=open(pArchivoNuevo, "w")
    patron=r'"[^"]*"|\'[^\']*\'|[a-zA-Z_]\w*|\s+|[^\w\s]' #ER que separa la línea en varias partes, reconociendo palabras, textos entre comillas, espacios y saltos de línea y símbolos.
    reemplazados=0
    totalPalabras=0
    for linea in archivoATraducir:
        partes=re.findall(patron, linea) #A la variable parte se le asigna cada patrón de la ER encontrado. 
        lineaNueva=""
        for parte in partes:
            reemplazada=parte
            if not parte.isspace(): #Evita los espacios.
                totalPalabras+=1
                for token in pTokensActuales:
                    if parte==token[0]:
                        reemplazada=token[1]
                        reemplazados+=1
                        registrarToken(conteo, token[0], token[1])
                        registrarAccion(bitacora, f"Se hizo el reemplazo de : {token[0]} → {token[1]}", "bitacora.txt")
            lineaNueva+=reemplazada
        archivoNuevo.write(lineaNueva)
    archivoATraducir.close()
    archivoNuevo.close()
    registrarAccion(bitacora,f"Traducción completada con {reemplazados} reemplazos realizados.","bitacora.txt")
    return reemplazados, totalPalabras

def generarCSV(conteo,bitacora):
    """
    Funcionamiento: Genera un archivo CSV con la información de los reemplazos realizados durante la traducción.
    Entradas: 
    conteo -Explicación: Es el diccionario que almacena las palabras originales, el token de reemplazo y la cantidad de veces que fueron reemplazadas.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas en el sistema.
    Salidas: 
    Ninguna salida -Explicación: La función únicamente crea un archivo CSV con la información de los reemplazos realizados.
    """
    archivo = open("reporteReemplazos.csv", "w", newline="", encoding="utf-8") #Crea el archivo. 
    writer = csv.writer(archivo) #Writer permite que se pueda escribir en el archivo.
    writer.writerow(["Palabra Original", "Token de reemplazo", "Cantidad de reemplazos"]) #Encabezados de las columnas.
    for palabra in conteo:
        token = conteo[palabra]["token"]
        cantidad = conteo[palabra]["cantidad"]
        writer.writerow([palabra, token, cantidad]) #Escribe una fila dentro del csv.  
    archivo.close() 
    registrarAccion(bitacora, f"Se generó el csv con los reemplazos.", "bitacora.txt")
    
def registrarToken(conteo, palabra, token):
    """
    Funcionamiento: Guarda y acumula la cantidad de reemplazos realizados durante la traducción.
    Entradas:
    conteo -Explicación: Es el diccionario donde se almacenan las estadísticas de reemplazos.
    palabra -Explicación: Es la palabra original encontrada en el archivo.
    token -Explicación: Es el token que reemplaza a la palabra original.
    Salidas:
    conteo (Tipo: Diccionario) -Explicación: Se actualiza el diccionario con la cantidad de reemplazos realizados para cada palabra.
    """
    if palabra not in conteo: #Si la palabra aún no se reemplazó.
        conteo[palabra] = {"token": token,"cantidad": 1} #Guarda la palabra, el token que se usó y el contador inicia en 1.
    else:
        conteo[palabra]["cantidad"] += 1 #si sí existía le suma 1 a los reemplazos.


def generarReporteHTML(titulo,conteo, duracion, totalReemplazos, porcentaje,bitacora):
    """
    Funcionamiento: Genera un archivo HTML con un reporte de los reemplazos realizados durante la traducción.
    Entradas:
    titulo -Explicación: Es el título que aparecerá en la pestaña del navegador.
    conteo -Explicación: Es el diccionario que almacena las palabras originales, los tokens y la cantidad de reemplazos.
    duracion -Explicación: Es el tiempo total que tardó el procesamiento.
    totalReemplazos -Explicación: Es la cantidad total de reemplazos realizados.
    porcentaje -Explicación: Es el porcentaje de palabras reemplazadas durante la traducción.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas en el sistema.
    Salidas:
    Ninguna salida -Explicación: La función crea un archivo HTML con el reporte generado.
    """
    fechaHora = datetime.now() 
    fechaMostrar = fechaHora.strftime("%d/%m/%Y %H:%M:%S")#Es la fecha que se va a mostrar dentro del HTML, por eso lo convierte a string.
    nombreArchivo = fechaHora.strftime("reporteHTML_%d-%m-%y-%H-%M-%S.html") #Aqui usamos guiones porque "/" y ":" no funcionan e investigando vimos que es por que windows lo puede identificar de otra manera 
    archivoHTML = open(nombreArchivo, "w", encoding="utf-8") #utf-8 permite escribit tíldes, símbolos y caracteres especiales.
    # Este f""" sirve para escribir muchas líneas seguidas  y meter variables dentro del texto
    archivoHTML.write(f"""  
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <!-- Título de la pestaña -->
        <title>{titulo}</title>
        <style>
            body {{font-family: Arial;
                margin: 30px;
                background-color: white;
                color: black}}
            h1 {{text-align: center;
                color: black;}}
            h2 {{text-align: center;
                color: red;}}
            p {{font-size: 18px;}}
            /* Tabla */
            table {{width: 100%;
                border-collapse: collapse;
                margin-top: 20px;}}
            /* Bordes */
            table, th, td {{border: 1px solid black;}}
            /* Encabezados */
            th {{background-color: black;
                color: white;
                padding: 10px;}}
            /* Celdas */
            td {{padding: 10px;
                text-align: center;}}
            /* Filas alternas */
            tr:nth-child(even) {{background-color: #e6e6e6;}}
            tr:nth-child(odd) {{background-color: white;}}
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
            </tr>""")
    for palabra in conteo:
            token = conteo[palabra]["token"]
            cantidad = conteo[palabra]["cantidad"]
            archivoHTML.write(f"""
            <tr>
                <td>{palabra}</td>
                <td>{token}</td>
                <td>{cantidad}</td>
            </tr>""")
    archivoHTML.write("""</table></body></html>""")
    archivoHTML.close()#aqui se cierra ya el archivo

def guardarBitacora(nombreArchivo, bitacora):
    """
    Funcionamiento: Guarda la bitácora en un archivo binario utilizando pickle.
    Entradas:
    nombreArchivo -Explicación: Es el nombre del archivo donde se almacenará la bitácora.
    bitacora -Explicación: Es la lista que contiene los registros de acciones realizadas.
    Salidas:
    Ninguna salida -Explicación: La función únicamente guarda la información de la bitácora en un archivo.
    """
    archivo=open(nombreArchivo, "wb")
    pickle.dump(bitacora, archivo) #Guarda los datos en modo binario.
    archivo.close()

def cargarBitacora(nombreArchivo):
    """
    Funcionamiento: Carga la bitácora almacenada en un archivo binario utilizando pickle.
    Entradas:
    nombreArchivo -Explicación: Es el nombre del archivo donde está guardada la bitácora.
    Salidas:
    bitacora (Tipo: Lista) -Explicación: Contiene los registros cargados desde el archivo.
    [] (Tipo: Lista) -Explicación: Retorna una lista vacía si ocurre algún error al abrir o cargar el archivo.
    """
    try:
        archivo=open(nombreArchivo, "rb")
        bitacora=pickle.load(archivo) #Abre un archivo binario, reconstruye la la lista original y lo guarda en "bitacora"
        archivo.close()
        return bitacora
    except:
        return []
    
def registrarAccion(bitacora, descripcion, nombreArchivo):
    """
    Funcionamiento: Registra una acción en la bitácora junto con la fecha y hora en que ocurrió.
    Entradas:
    bitacora -Explicación: Es la lista donde se almacenan los registros de acciones realizadas.
    descripcion -Explicación: Es el texto que describe la acción realizada.
    nombreArchivo -Explicación: Es el nombre del archivo donde se guardará la bitácora actualizada.
    Salidas:
    Ninguna salida -Explicación: La función agrega un registro a la bitácora y guarda los cambios en el archivo.
    """
    fecha=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    registro=(fecha, descripcion)    
    bitacora.append(registro)    
    guardarBitacora(nombreArchivo, bitacora)

def buscarPorFecha(bitacora, fechaBuscada):
    """
    Funcionamiento: Busca registros dentro de la bitácora que coincidan con una fecha específica ingresada por el usuario. La búsqueda se realiza comparando el inicio de la cadena de fecha de cada registro.
    Entradas: 
    bitacora -Explicación: Es la lista que contiene todos los registros almacenados, donde cada registro es una tupla (fecha, descripción).
    fechaBuscada -Explicación: Es la fecha que el usuario desea buscar dentro de la bitácora.
    Salidas: 
    encontrados (Tipo: Lista de tuplas) -Explicación: Contiene todos los registros cuya fecha coincide (o inicia con) la fecha ingresada por el usuario.
    """
    encontrados=[]    
    for registro in bitacora:
        if registro[0].startswith(fechaBuscada): #Si la fecha del registro comienza con la fecha que ingresó el usuario.
            encontrados.append(registro)    
    return encontrados

def buscarPorPalabra(bitacora, palabra):
    """
    Funcionamiento: Busca en la bitácora los registros que contengan una palabra específica.
    Entradas: 
    bitacora -Explicación: Es la lista que contiene los registros almacenados en la bitácora.
    palabra -Explicación: Es la palabra que se desea buscar dentro de las descripciones de los registros.
    Salidas: 
    encontrados (Tipo: Lista) -Explicación: Contiene los registros de la bitácora en la cual la descripción incluye la palabra buscada.
    """
    encontrados=[]   
    for registro in bitacora:
        if palabra.lower() in registro[1].lower():
            encontrados.append(registro)   
    return encontrados

def mostrarRegistros(listaRegistros):
    """
    Funcionamiento: Muestra en pantalla los registros almacenados en una lista de registros.
    Entradas: 
    listaRegistros -Explicación: Es la lista que contiene los registros que se desean mostrar.
    Salidas: 
    Ninguna salida -Explicación: La función solo imprime los registros en pantalla y no retorna nada.
    """
    if len(listaRegistros)==0:
        print("No se encontraron registros almacenados.")
    else:
        for registro in listaRegistros:
            print(registro[0], "-", registro[1])