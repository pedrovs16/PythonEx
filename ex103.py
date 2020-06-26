def ficha(nome=0, gols=0):
    resposta = str
    if nome and gols != 0:
        resposta= f'O jogador {nome} marcou {gols}.'
    elif nome == 0 and gols != 0:
        resposta = f'O jogador desconhecido marcou {gols}.'
    elif nome != 0 and gols == 0:
        resposta = f'O jogador {nome} marcou nenhum gol.'
    elif nome == 0 and gols == 0:
        resposta = f'O jogador desconhecido marcou nenhum gol.'
    return resposta
print(ficha())
