from TareaProgramada1 import*
def opcionUno(bitacora):
    while True:
        pArchivo=input("Ingrese el nombre del archivo (incluyendo la extensión) que contiene los tokens (ejemplo: archivo.py): ").strip()
        if pArchivo=="":
            print("Debe ingresar algún archivo.")
            registrarAccion(bitacora, "No ingresó nombre de archivo en opción 1.", "bitacora.txt")
            continue
        break
    while True:
        pSeparador=input("Ingrese el separador de tokens que se utiliza en el archivo ingresado (ejemplo: = ): ").strip()
        if pSeparador=="":
            print("Debe ingresar al menos un separador.")
            registrarAccion(bitacora, "No ingresó separador en opción 1.","bitacora.txt")
            continue
        break
    tokens,reemplazados,lineasIncorrectas,mensaje=cargarArchivos(pArchivo, pSeparador, pTokensActuales, bitacora)                
    if mensaje:
        registrarAccion(bitacora, "Ocurrió un problema al cargar archivo: " + mensaje, "bitacora.txt")
        return mensaje
    registrarAccion(bitacora,"Archivo de tokens cargado correctamente: " + pArchivo,"bitacora.txt")
    if lineasIncorrectas:
        registrarAccion(bitacora,"Se encontraron " + str(len(lineasIncorrectas)) + " líneas incorrectas.","bitacora.txt")
        print("Las siguientes lineas no se agregaron ya que no contenían el separador ingresado: (",pSeparador,")")
        for linea in lineasIncorrectas:
            print(linea)
    if len(reemplazados)>0:
        registrarAccion(bitacora,"Se reemplazaron " + str(len(reemplazados)) + " tokens.","bitacora.txt")
        for token in reemplazados:
            print("Se reescribió el token de:", token)                   
    return "El archivo de tokens fue ingresado con éxito."

def opcionDos(pTokensActuales, bitacora):
    resultado=mostrarTokens(pTokensActuales)
    if resultado==[]:
        registrarAccion(bitacora,"No se pudieron mostrar tokens porque la lista está vacía.","bitacora.txt")
        return "No hay tokens almacenados actualmente, primero debe ingresar algún archivo o una lista de tokens."
    else:
        registrarAccion(bitacora,"Se mostraron correctamente los tokens almacenados.","bitacora.txt")
        return "\n".join(resultado)
    
def opcionTres(pTokensActuales,bitacora):
    while True:
        pCadena=input("Ingrese la lista de tokens (si desea cancelar la operación digite 1): ")    
        if pCadena=="1":
            registrarAccion(bitacora,"El usuario canceló la operación de agregar/modificar tokens.","bitacora.txt")
            return "Se canceló la operación."    
        if pCadena=="":
            print("No se puede proseguir con la operación, debe ingresar una lista de tokens, o al menos un token.")
            registrarAccion(bitacora,"No ingresó ninguna cadena de tokens.","bitacora.txt")
            continue
        break
    while True:
        pSeparadorTokens=input("Indique el separador que divide cada elemento de la lista (si solo es un token y no una lista ingrese un punto (.)): ").strip()
        if pSeparadorTokens=="":
            print("Debe ingresar al menos un separador.")
            registrarAccion(bitacora,"No ingresó separador de tokens.","bitacora.txt")
            continue
        if pSeparadorTokens==pSepararCadena:
            print("Los separadores de cada elemento de la lista y los de cada token no pueden ser iguales.")
            registrarAccion(bitacora,"Ingresó separadores iguales para tokens y token/valor.","bitacora.txt")
            continue
        break
    while True:          
        pSepararCadena=input("Indique el separador que utilizado para separar los tokens con su respectivo valor: ").strip()
        if pSepararCadena=="":
            print("Debe ingresar al menos un separador válido.")
            registrarAccion(bitacora,"No ingresó separador token/valor.","bitacora.txt")
            continue
        break      
    pTokensActuales, agregados, modificados=agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales)
    if not agregados and not modificados:
        registrarAccion(bitacora,"No se agregó ni modificó ningún token.","bitacora.txt")
        return "No se procesó ningún token. Los tokens ya se encontraban agregados y no se realizó ningun cambio.\n Revise si ya se encontraban almacenados o verifique si el separador es el correcto."
    mensajes=[]
    for token in agregados:
        mensajes.append(f"Se agregó el token: '{token}'")    
    for token in modificados:
        mensajes.append(f"Se modificó el token: '{token}'")
        registrarAccion(bitacora,f"Se agregaron {len(agregados)} tokens y se modificaron {len(modificados)} tokens.","bitacora.txt")
    return "\n".join(mensajes), pTokensActuales

def opcionCinco(pTokensActuales,bitacora):
    if not pTokensActuales:
        registrarAccion(bitacora,"Se intentó traducir un archivo sin tokens almacenados.","bitacora.txt")
        return "No hay tokens almacenados actualmente, debe ingresar algún archivo o una lista de tokens primero."   
    while True:
        pArchivoATraducir=input("Ingrese el nombre archivo que desea traducir (Ejemplo: archivo.py): ").strip()
        if pArchivoATraducir=="":
            registrarAccion(bitacora,"No ingresó archivo para traducir.","bitacora.txt")
            print("Debe ingresar un archivo.")
            continue
        valido,mensaje=archivoExiste(pArchivoATraducir)
        if not valido:
            registrarAccion(bitacora,f"El archivo '{pArchivoATraducir}' no existe.","bitacora.txt")
            print(mensaje)
        break
    while True:
        pArchivoNuevo=input("Ingrese el nombre del nuevo archivo traducido (Ejemplo: traducido.py): ").strip()
        if pArchivoNuevo=="":
            registrarAccion(bitacora,"No ingresó nombre para el archivo traducido.","bitacora.txt")
            print("Debe ingresar un nombre de archivo válido.")
            continue
        break
    traducirArchivo(pArchivoATraducir, pArchivoNuevo, pTokensActuales, bitacora)    
    registrarAccion(bitacora,f"Se tradujo el archivo.  Nuevo archivo: '{pArchivoNuevo}'.","bitacora.txt")
    return f"El archivo se tradujo correctamente y fue agregado como: {pArchivoNuevo}"  