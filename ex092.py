pessoa = {}
pessoa['nome'] = input('Digite o seu nome: ')
pessoa['nasc'] = int(input('Digite o ano que nasceste: '))
pessoa['carteira'] = int(input('Digite sua carteira de trabalho,se nao tiver digite 0: '))
pessoa['idade'] = 2020 - pessoa["nasc"]
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = int(input('Digite o seu salário: '))
    print(f'Seu nome é {pessoa["nome"]}. ')
    print(f'Sua idade é {pessoa["idade"]}.')
    print(f'Seu ctps é {pessoa["carteira"]}.')
    print(f'Foi contratada em {pessoa["contratacao"]}.')
    print(f'Seu salário é de {pessoa["salario"]}.')
    print(f'Vai se aposentar com {pessoa["idade"] + 50 - (2020 - pessoa["contratacao"])}')
else:
    print(f'Seu nome é {pessoa["nome"]}. ')
    print(f'Sua idade é {pessoa["idade"]}.')
    print(f'Seu ctps é {pessoa["carteira"]}.')



