import arquivo as pc
nome_maquina = "Black"
pc.saudacoes(nome_maquina)
while True:
    texto = pc.recebeTexto('Black')
    resposta = pc.buscaResposta(nome_maquina, texto)
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break