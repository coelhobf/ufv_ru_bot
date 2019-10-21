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
        texto = ""
        
        for dado in dados:
            texto += '\n' + dado
    except:
        texto = "[ERRO NA PUBLICAÇÃO]"

    return texto