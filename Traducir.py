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
    