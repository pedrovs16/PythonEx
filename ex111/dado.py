def leiaDinheiro(pergunta):
    resultado = 'f'
    while True:
        resultado = input(pergunta)
        if resultado.isnumeric() is True:
            break
        print('Não é um número tente novamente.')
    resultadoPronto = int(resultado)
    return resultadoPronto