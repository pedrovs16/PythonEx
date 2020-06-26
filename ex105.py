def notas(*num, sit=0):
    """

    :param num: valores de nota
    :param sit: se True apresenta a situação do boletim se False nao apresenta
    :return: dicionario um dict() com varias infos das notas
    """
    soma = 0
    count = 0
    for c in num:
        soma += c
        count += 1
    media = soma/count


    situacao = str
    if media >= 7:
        situacao = 'Boa'
    else:
        situacao = 'Ruim'
    dicionario = {}
    if sit == True:
        dicionario = {
            'numero de notas': len(num),
            'notamax': max(num),
            'notamin': min(num),
            'media': media,
            'situação': situacao
        }
    if sit == False:
        dicionario = {
            'numero de notas': len(num),
            'notamax': max(num),
            'notamin': min(num),
            'media': media,
        }
    return dicionario

print(notas(5,4,3))
