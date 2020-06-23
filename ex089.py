lista = [[], [], [], []]
nome = str
resposta = str
nota1 = int
nota2 = int
estilo = 0
resultado = 0

while resposta != 'N' and resposta != 'n':
    lista[estilo].insert(0, input('Digite o nome do aluno:'))
    estilo += 1
    nota1 = int(input('Digite a Av1 do aluno: '))
    lista[estilo].insert(0, nota1)
    estilo += 1
    nota2 = int(input('Digite a Av2 do aluno: '))
    lista[estilo].insert(0,nota2)
    estilo += 1
    lista[estilo].insert(0,(nota1 + nota2)/2)

    resposta = (input('Queres continuar? [S/N] '))
    resultado += 1
    estilo = 0
print(lista)
print('  NOME    AV1    AV2   MÉDIA')
for c in range(0,resultado):
    print(f'{lista[0][c]}---{lista[1][c]}----{lista[2][c]}----{lista[3][c]}')