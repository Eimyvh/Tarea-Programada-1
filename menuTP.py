from TareaProgramada1 import*
pTokensActuales=[]
while True:
    print("\n" + "="*50)
    print("MENU".center(50,"*"))
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
                pArchivo=input("Ingrese el nombre del archivo que contiene los tokens (con su extensión): ")
                if pArchivo=="":
                    print("Debe ingresar un archivo.")
                    continue
                pSeparador=input("Ingrese el separador que se utiliza en el archivo ingresado: ")
                if pSeparador=="":
                    print("Debe ingresar un separador.")
                    continue
                valido,mensaje=validarArchivo(pArchivo, pSeparador)
                tokens=[]
                reemplazados=[]
                if not valido:
                    print(mensaje)
                else:
                    tokens,reemplazados=cargarArchivos(pArchivo, pSeparador, pTokensActuales)                
                    if len(reemplazados)>0:
                        for token in reemplazados:
                            print("Se reescribió el token de:", token)                   
                    print("El archivo de tokens fue ingresado con éxito.")
    elif opcion=="2":
                resultado=mostrarTokens (pTokensActuales)
                if resultado==[]:
                    print("No hay tokens almacenados actualmente, debe ingresar algún archivo o una lista de tokens primero.")
                else:
                    print("\n".join(resultado))
    elif opcion=="3":
            pCadena=input("Ingrese la lista de tokens (si desea cancelar la operación, digite 1): ")
            if pCadena=="1":
                   print("Se canceló la operación.")
                   continue
            elif pCadena=="":
                  print ("No se puede seguir con la operación, debe ingresar una lista de tokens.")
                  continue
            else:
                pSeparadorTokens=input("Indique el separador que divide cada elemento de la lista (si solo es un token y no una lista ingrese un punto (.)): ")
                if pSeparadorTokens=="":
                    print("Debe ingresar algún separador.")
                    continue
                pSepararCadena=input("Indique el separador que aparte los tokens con su respectivo valor: ")
                if pSepararCadena=="":
                    print("Debe ingresar un separador válido.")
                    continue
                if pSeparadorTokens==pSepararCadena:
                    print("Los separadores no pueden ser iguales.")
                    continue
                pTokensActuales,agregados,modificados=agregarOModificar(pCadena, pSeparadorTokens, pSepararCadena, pTokensActuales)
                if len(agregados)==0 and len(modificados)==0:
                    print("No se pudieron procesar tokens válidos.")
                else:
                    for token in agregados:
                        print(f"Se agregó el token: '{token}'")
                    for token in modificados:
                        print(f"Se modificó el token:'{token}'") 