dicionario = {}
dicionario['nome'] = input('Digite o nome do aluno: ')
dicionario['media'] = int(input(f'Digite a media de {dicionario["nome"]}: '))
if dicionario['media'] >= 7:
    dicionario['resultado'] = 'Aprovado'
else:
    dicionario['resultado'] = 'Reprovado'
print(f'O aluno {dicionario["nome"]} com a média {dicionario["media"]} foi {dicionario["resultado"]}.')