def saudacoes(Black):
    import random
    frases = ["Bom dia, meu nome é Black", "Como vai?", "tudo bem?"]
    print(frases[random.randint(0,2)])

def recebeTexto(Black):
    texto = "Cliente: " + input("Cliente: ")
    palavraProibida = ["burro", 'corno', "desgraçado", "caralho", "viado"]
    for p in palavraProibida:
        if p in texto:
            print("Olha boca se não vou seguir você até o inferno")
            return recebeTexto()
        return texto

def buscaResposta (nome, texto):
    with open("BancoDeDados.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "": 
                if texto.replace("Cliente: ","") == "Tchau":
                    print(nome+": volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
                else:
                    print("Me desculpe, não sei o que falar")
                    conhecimento.write("\n" + texto)
                    resposta_user= input("O que esperava?\n")
                    conhecimento.write("\n" +"Chatbot: "+resposta_user)
                    return "Hum..."
                
def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"