def cargarArchivos (pArchivo, pSeparador, pTokensActuales):    
    try:
            archivo=open(pArchivo, "r" )     
            for linea in archivo: #Recorre cada linea.
                linea=linea.strip() #Elimina los espacios al final y principio antes de separarlas.
                partes=linea.split(pSeparador) #Separa con el separador que haya ingresado el usuario.
                token = partes[0]
                traduccion = partes[1]
                reemplazado = False #Bandera para cuando se hagan reemplazos.
                for i in range(len(pTokensActuales)): #Recorre la lista de tokens usando índices.
                    if pTokensActuales[i][0] == token: #Compara el token actual con el que está en el archivo.
                        if pTokensActuales[i][1] != traduccion: #Si la traducción del token es diferente al actual, se reemplaza.
                            print("Se reescribió el token de:", token)
                            pTokensActuales[i] = (token, traduccion)
                        reemplazado = True #Indica que el token ya existe en la lista de tokens (ya hubo reemplazo).
                if reemplazado == False:
                    pTokensActuales.append((token, traduccion)) #Si no el token no estaba en la lista solo se agrega como un nuevo archivo para las listas.             
            archivo.close()
            return pTokensActuales       
    except FileNotFoundError: #En caso de que no exista el archivo.
        return "El archivo que ingresó no existe."