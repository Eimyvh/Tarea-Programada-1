#Elaborado por: Eimy Vega Hidalgo y Zaid Chaves Durán.
#Fecha de creación:26/04/2026
#Ultima modificación:12/05/2026
#Versión: Python 3.14 (64-bit)
from tokens import*

def opcionUno(bitacora):
    """
    Funcionamiento: Solicita al usuario un archivo que contenga tokens y el separador utilizado en el archivo. Luego carga los tokens válidos y guarda los registros en una bitácora.
    Entradas: 
    bitacora -Explicación: Es la lista donde se almacenan los registros de acciones realizadas por el usuario dentro del programa.
    Salidas: 
    mensaje (Tipo: String) -Explicación: Muestra un mensaje indicando si ocurrió algún error al cargar el archivo o si la operación fue realizada correctamente.
    lineasIncorrectas (Tipo: Lista) -Explicación: Contiene las líneas que no se agregaron porque no tenían el formato correcto o no contenían el separador indicado.
    reemplazados (Tipo: Lista) -Explicación: Almacena los tokens que ya existían y fueron reemplazados por nuevos valores.
    """
    while True:
        pArchivo=input("Ingrese el nombre del archivo (incluyendo la extensión) que contiene los tokens (ejemplo: archivo.py): ").strip()
        if opcionVacia(pArchivo):
            print("Debe ingresar algún archivo.")
            registrarAccion(bitacora, "No ingresó nombre de archivo en opción 1.", "bitacora.txt")
            continue
        break
    while True:
        pSeparador=input("Escriba el separador de tokens que se utiliza en el archivo ingresado (ejemplo: = ): ").strip()
        if opcionVacia(pSeparador):
            print("Debe ingresar al menos un separador.")
            registrarAccion(bitacora, "No ingresó separador en opción 1.","bitacora.txt")
            continue
        break
    tokens,reemplazados,lineasIncorrectas,mensaje=cargarArchivos(pArchivo, pSeparador, pTokensActuales, bitacora)                
    if mensaje:
        registrarAccion(bitacora, "Ocurrió un problema al cargar archivo: " + mensaje, "bitacora.txt")
        return mensaje
    registrarAccion(bitacora,"El archivo de tokens se cargó correctamente: " + pArchivo,"bitacora.txt")
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
    """
    Funcionamiento: Muestra los tokens almacenados actualmente en un formato más legible para el usuario. 
    Además, registra en la bitácora si los tokens pudieron mostrarse correctamente o si la lista estaba vacía.
    Entradas: 
    pTokensActuales -Explicación: Es la lista que contiene los tokens y sus respectivas traducciones almacenadas actualmente.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas por el usuario dentro del programa.
    Salidas: 
    resultado (Tipo: String) -Explicación: Devuelve los tokens almacenados en un formato organizado y separado por líneas para facilitar su lectura.
    mensaje (Tipo: String) -Explicación: Muestra un mensaje indicando que no existen tokens almacenados actualmente.
    """
    resultado=mostrarTokens(pTokensActuales,bitacora)
    if opcionVacia(resultado):
        registrarAccion(bitacora,"No se pudieron mostrar tokens porque la lista está vacía.","bitacora.txt")
        return "No hay tokens almacenados actualmente, primero debe ingresar algún archivo o una lista de tokens."
    else:
        registrarAccion(bitacora,"Se mostraron correctamente los tokens almacenados.","bitacora.txt")
        return "\n".join(resultado)
    
def opcionTres(pTokensActuales,bitacora):
    """
    Funcionamiento: Solicita al usuario una lista de tokens y sus traducciones para agregarlos o modificarlos 
    dentro de los tokens almacenados actualmente. Además, valida los separadores ingresados y registra las acciones 
    realizadas en la bitácora.
    Entradas: 
    pTokensActuales -Explicación: Es la lista que contiene los tokens y traducciones almacenados actualmente.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas por el usuario dentro del programa.
    Salidas: 
    mensaje (Tipo: String) -Explicación: Indica si la operación fue cancelada, si no se procesó ningún token o si los tokens fueron agregados/modificados correctamente.
    agregados (Tipo: Lista) -Explicación: Contiene los tokens que fueron agregados por primera vez.
    modificados (Tipo: Lista) -Explicación: Contiene los tokens que ya existían y fueron modificados.
    pTokensActuales (Tipo: Lista de tuplas) -Explicación: Lista actualizada con los nuevos tokens agregados o modificados.
    """
    while True:
        pCadena=input("Ingrese la lista de tokens (si desea cancelar la operación digite 1): ")    
        if pCadena=="1":
            registrarAccion(bitacora,"El usuario canceló la operación de agregar/modificar tokens.","bitacora.txt")
            return "Se canceló la operación."    
        if opcionVacia(pCadena):
            print("No se puede seguir con la operación, debe ingresar una lista de tokens, o al menos un token.")
            registrarAccion(bitacora,"No ingresó ninguna cadena de tokens.","bitacora.txt")
            continue
        break
    while True:
        pSeparadorTokens=input("Indique el separador que divide cada elemento de la lista (si solo es un token y no una lista ingrese un punto (.)): ").strip()
        if opcionVacia(pSeparadorTokens):
            print("Debe ingresar al menos un separador.")
            registrarAccion(bitacora,"No ingresó separador de tokens.","bitacora.txt")
            continue
        break
    while True:          
        pSepararCadena=input("Indique el separador que utilizado para separar los tokens con su respectivo valor: ").strip()
        if opcionVacia(pSepararCadena):
            print("Debe ingresar al menos un separador válido.")
            registrarAccion(bitacora,"No ingresó separador token/valor.","bitacora.txt")
            continue
        if pSeparadorTokens==pSepararCadena:
            print("Los separadores de cada elemento de la lista y los de cada token no pueden ser iguales.")
            registrarAccion(bitacora,"Ingresó separadores iguales para tokens y token/valor.","bitacora.txt")
            continue
        break      
    pTokensActuales, agregados, modificados=agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales, bitacora)
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
    """
    Funcionamiento: Solicita al usuario un archivo para traducir utilizando los tokens almacenados actualmente. 
    Además, valida que el archivo exista, solicita el nombre del nuevo archivo traducido y registra las acciones 
    realizadas en la bitácora.
    Entradas: 
    pTokensActuales -Explicación: Es la lista que contiene los tokens y traducciones almacenados actualmente y que se utilizarán para realizar la traducción.
    bitacora -Explicación: Es la lista donde se registran las acciones realizadas por el usuario dentro del programa.
    Salidas: 
    mensaje (Tipo: String) -Explicación: Indica si la traducción se realizó correctamente o si ocurrió algún problema durante el proceso.
    totalReemplazos (Tipo: Int) -Explicación: Contiene la cantidad total de palabras que fueron reemplazadas durante la traducción del archivo.
    totalPalabras (Tipo: Int) -Explicación: Contiene la cantidad total de palabras procesadas en el archivo traducido.
    """
    if not pTokensActuales:
        registrarAccion(bitacora,"Se intentó traducir un archivo sin tokens almacenados.","bitacora.txt")
        return "No hay tokens almacenados actualmente, debe ingresar algún archivo o una lista de tokens primero."   
    while True:
        pArchivoATraducir=input("Ingrese el nombre archivo que desea traducir (Ejemplo: archivo.py): ").strip()
        if opcionVacia(pArchivoATraducir):
            registrarAccion(bitacora,"No ingresó archivo para traducir.","bitacora.txt")
            print("Debe ingresar un archivo.")
            continue
        valido,mensaje=archivoExiste(pArchivoATraducir)
        if not valido:
            registrarAccion(bitacora,f"El archivo '{pArchivoATraducir}' no existía.","bitacora.txt")
            print(mensaje)
            continue
        break
    while True:
        pArchivoNuevo=input("Ingrese el nombre del nuevo archivo traducido (Ejemplo: traducido.py): ").strip()
        if opcionVacia(pArchivoNuevo):
            registrarAccion(bitacora,"No ingresó nombre para el archivo traducido.","bitacora.txt")
            print("Debe ingresar un nombre de archivo válido.")
            continue
        break
    totalReemplazos,totalPalabras=traducirArchivo(pArchivoATraducir, pArchivoNuevo, pTokensActuales, bitacora, conteo)    
    registrarAccion(bitacora,f"Se tradujo el archivo.  Nuevo archivo: '{pArchivoNuevo}'.","bitacora.txt")
    mensaje= f"El archivo se tradujo correctamente y fue agregado como: {pArchivoNuevo}"    
    return mensaje, totalReemplazos,totalPalabras

def submenuBitacora(bitacora):
    """
    Funcionamiento: Muestra un submenú que permite buscar registros dentro de la bitácora del sistema 
    ya sea por una fecha específica o por palabras clave. También permite salir del submenú.
    Entradas: 
    bitacora -Explicación: Es la lista que contiene los registros de acciones realizadas dentro del programa junto con su fecha y descripción.
    Salidas: 
    encontrados (Tipo: Lista) -Explicación: Contiene los registros de la bitácora que coinciden con la fecha o palabra clave ingresada por el usuario.
    mensaje (Tipo: String) -Explicación: Indica si no se encontraron registros relacionados con la búsqueda realizada.
    registro (Tipo: String) -Explicación: Muestra la fecha y descripción de cada acción encontrada dentro de la bitácora.
    """
    while True:
        print("\n==Submenú de bitácora del sistema==")
        print("1) Acciones por día escogido.")
        print("2) Acciones por palabras clave.")
        print("3) Salir del submenú.")
        while True:
            opcion=input("Seleccione una opción: ").strip()   
            if opcion not in ["1", "2", "3"]:
                print("Debe ingresar 1, 2 o 3.")
                continue
            break
        if opcion == "1":
            while True:
                fecha = input("Ingrese la fecha en el siguiente formato: AAAA-MM-DD (con guiones) (Donde: AAAA=Año, MM=Mes, DD=Día): ").strip()
                if opcionVacia(fecha):
                    print("Debe ingresar una fecha para buscar el registro en la bitácora.")
                mensaje=validarFecha(fecha)
                if mensaje:
                    print(mensaje)
                break
            encontrados=[]            
            for registro in bitacora:
                if registro[0].startswith(fecha):
                    encontrados.append(registro)            
            if len(encontrados)==0:
                return "No se encontraron registros sobre acciones en esa fecha."
            else:
                for r in encontrados:
                    print(r[0], "-", r[1])   
        elif opcion=="2":
            while True:
                palabra=input("Ingrese la palabra clave que desea buscar en los registros: ").strip().lower()
                if palabra == "":
                    print("Debe ingresar una palabra.")
                    continue
                break
            encontrados = []
            for registro in bitacora:
                if palabra in registro[1].lower():
                        encontrados.append(registro)            
                if len(encontrados)==0:
                    print("No se encontraron registros sobre acciones con su palabra clave.")
                else:
                    for r in encontrados:
                        return r[0], "-", r[1]       
        elif opcion=="3":
            print("Ha cerrado el programa.")
            break        
    
def validarFecha(fecha):
    """
    Funcionamiento: Valida que la fecha ingresada por el usuario tenga el formato correcto, 
    contenga únicamente números y represente una fecha válida según el calendario.
    Entradas: 
    fecha -Explicación: Es la fecha ingresada por el usuario en formato AAAA-MM-DD que se desea validar.
    Salidas: 
    mensaje (Tipo: String) -Explicación: Devuelve un mensaje indicando el error encontrado en caso de que la fecha sea inválida.
    None (Tipo: NoneType) -Explicación: Se retorna cuando la fecha ingresada cumple correctamente con todas las validaciones.
    """
    if "-" not in fecha:
        return "El separador de la fecha debe ser un guión ( - )."
    partes=fecha.split("-")
    if len(partes)!=3:
        return "La fecha debe contener año, mes y día."
    año=partes[0]
    mes=partes[1]
    dia=partes[2]
    if not (año.isdigit() and mes.isdigit() and dia.isdigit()):
        return "La fecha solo debe contener números."
    año=int(año)
    mes=int(mes)
    dia=int(dia)
    añoActual=datetime.now().year
    if año>añoActual:
        return "El año no puede ser mayor al actual."
    if mes<1 or mes>12:
        return "El mes debe estar entre 1 y 12."
    if dia<1:
        return "El día debe ser mayor que 0."
    meses30=[4, 6, 9, 11]
    if mes in meses30 and dia>30:
        return "No se encontró nada ya que ese mes solo tiene 30 días."
    elif mes==2:
        bisiesto=False
        if (año % 4==0 and año %100!=0) or (año % 400==0):
            bisiesto=True
        if bisiesto and dia>29:
            return "Febrero es un año bisiesto, solo tiene 29 días, por lo que ese día no se pudieron haber realizado registros."
        elif not bisiesto and dia>28:
            return "Febrero solo tiene 28 días, por lo que no existen registros ese día."
    elif dia>31:
        return "Ese mes solo tiene 31 días, no existen rregistros de ese día."
    return None 

########################################################################################     MENU     ##################################################################################################
import time
pTokensActuales=[]
conteo = {}
totalReemplazos = 0
totalPalabras = 0
inicioPrograma = time.time()#La hora en la que se inició el programa.
bitacora=cargarBitacora("bitacora.txt")
while True:
    print("\n" + "="*50)
    print("Menú principal".center(50,"*"))
    print("="*50)   
    print(" 1) Cargar tokens.")
    print(" 2) Mostrar tokens.")
    print(" 3) Agregar/modificar token.")
    print(" 4) Guardar tokens.")
    print(" 5) Traducir codigo.")
    print(" 6) Generar CSV.")
    print(" 7) Generar HTML.")
    print(" 8) Submenú de bitácota del sistema.")
    print(" 9) Salir.")
    print("="*50)
    opcion=input("Ingresa tu opción: ")
    if opcion=="1":
        registrarAccion(bitacora, "Seleccionó la opción 1 del menú principal: Cargar tokens", "bitacora.txt")
        resultado=opcionUno(bitacora)
        if resultado:
            print(resultado)               
    elif opcion=="2":
        registrarAccion(bitacora, "Seleccionó la opción 2 del menú principal: Mostrar tokens", "bitacora.txt")
        resultado=opcionDos(pTokensActuales,bitacora)
        print(resultado)
    elif opcion=="3":
        registrarAccion(bitacora, "Seleccionó la opción 3 del menú principal: Agregar/modificar token", "bitacora.txt")
        resultado=opcionTres(pTokensActuales,bitacora)
        if isinstance(resultado, tuple):
            mensaje, pTokensActuales=resultado
            print(mensaje)
        else:
            print(resultado)                    
    elif opcion=="4":
        registrarAccion(bitacora, "Seleccionó la opción 4 del menú principal: Guardar tokens", "bitacora.txt")
        while True:
            pArchivoN=input("Indique el archivo con la extensión en el que desea guardar las configuraciones actuales de los tokens (Ejemplo: archivo.txt): ")
            if opcionVacia(pArchivoN):
                registrarAccion(bitacora,"No ingresó nombre de archivo para guardar tokens.","bitacora.txt")
                print("Debe ingresar un nombre de archivo.")
                continue
            break
        while True:    
            pSeparadorInterno=input("Ingrese el separador que desea utilizar para dividir los tokens (Ejemplo: ->  ): ")
            if opcionVacia(pSeparadorInterno):
                registrarAccion(bitacora,"No ingresó separador interno para guardar tokens.","bitacora.txt")
                print("Debe ingresar un separador.")
                continue
            break
        guardarTokensEnArchivo(pArchivoN,pSeparadorInterno,pTokensActuales,bitacora)
        print("Los archivos fueron guardados exitosamente en el archivo llamado: ",pArchivoN)
    elif opcion=="5":
        registrarAccion(bitacora, "Seleccionó la opción 5 del menú principal: Traducir código", "bitacora.txt")
        resultado=opcionCinco(pTokensActuales,bitacora)
        if isinstance(resultado, tuple):
            mensaje, totalReemplazos, totalPalabras = resultado
            print(mensaje)
        else:
            print(resultado)
    elif opcion == "6":
        generarCSV(conteo,bitacora)
        registrarAccion(bitacora, "Seleccionó la opción 6 del menú principal: Generar CSV", "bitacora.txt")
        print("Archivo csv con registros de reemplazos de tokens creado exitosamente")
    elif opcion == "7":
        registrarAccion(bitacora, "Seleccionó la opción 7 del menú principal: Generar HTML", "bitacora.txt")
        titulo = input("Escriba el título que desea ponerle al reporte HTML: ")
        while True:
            if opcionVacia(titulo):
                print("Debe ingresar un título.")
                continue
            break
        duracion = round(time.time() - inicioPrograma, 2)
        if totalPalabras > 0:
            porcentaje = round((totalReemplazos / totalPalabras) * 100, 2)
        else:
            porcentaje = 0
        generarReporteHTML(titulo,conteo,duracion,totalReemplazos,porcentaje,bitacora)
        print("Se creó el archivo HTML con éxito.")
    elif opcion == "8":
            registrarAccion(bitacora, "Ingresó al submenú de bitácora", "bitacora.txt")
            submenuBitacora(bitacora)
    elif opcion == "9":
        registrarAccion(bitacora, "Salió del programa", "bitacora.txt")
        print("Saliste del menú principal.")
        break
    else:
        print("Ingrese una opción válida del menú (del 1 al 9).")