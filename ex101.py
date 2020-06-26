def voto(nascimento):
    resposta = str
    idade = 2020 - nascimento
    if idade > 15 and idade < 18 or idade > 65:
        resposta = f'Você tem {idade} anos seu voto é opcional'
    elif idade < 16:
        resposta = f'Você tem {idade} anos, não pode votar'
    elif idade > 17:
        resposta = f'Você tem {idade} anos seu voto é obrigatório'
    return resposta
valor = int(input('Digite o ano que vc nasceu: '))
resposta = voto(valor)
print(resposta)
