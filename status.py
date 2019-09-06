def textoAlmoco(dados):
    try:
        texto = "\n"
        texto += "Principal: " + dados[0] + "\n"
        texto += "Vegano: " + dados[1] + "\n"
        texto += "\n"
        texto += "Guarnição: " + dados[2] + "\n"
        texto += "Saladas: " + dados[3] + "\n"
        texto += "Sobremesa: " + dados[4]
    except:
        texto = "[ERRO NA PUBLICAÇÃO]"

    return texto

def textoJantar(dados):
    try:
        texto = "\n"
        texto += "Principal: " + dados[0] + "\n"
        texto += "Vegano: " + dados[1] + "\n"
        texto += "\n"
        texto += "Guarnição: " + dados[2] + "\n"
        texto += "Saladas: " + dados[3] + "\n"
        texto += "Sobremesa: " + dados[4]
    except:
        texto = "[ERRO NA PUBLICAÇÃO]"
    
    return texto

def textoLanche(dados):
    try:
        texto = "\n"
        texto += dados[0] + "\n"
        texto += dados[1] + "\n"
        texto += dados[2] + "\n"
        texto += dados[3]
    except:
        texto = "[ERRO NA PUBLICAÇÃO]"

    return texto