def textoAlmoco(dados):
    texto = ""
    texto += "ALMOÇO\n"
    texto += "\n"
    texto += "Principal: " + dados[0] + "\n"
    texto += "Vegano: " + dados[1] + "\n"
    texto += "\n"
    texto += "Guarnição: " + dados[2] + "\n"
    texto += "Saladas: " + dados[3] + "\n"
    texto += "Sobremesa: " + dados[4]

    return texto

def textoJantar(dados):
    texto = ""
    texto += "JANTAR\n"
    texto += "\n"
    texto += "Principal: " + dados[0] + "\n"
    texto += "Vegano: " + dados[1] + "\n"
    texto += "\n"
    texto += "Guarnição: " + dados[2] + "\n"
    texto += "Saladas: " + dados[3] + "\n"
    texto += "Sobremesa: " + dados[4]
    
    return texto

def textoLanche(dados):
    texto = ""
    texto += "LANCHE\n"
    texto += "\n"
    texto += dados[0] + "\n"
    texto += dados[1] + "\n"
    texto += dados[2] + "\n"
    texto += dados[3]

    return texto