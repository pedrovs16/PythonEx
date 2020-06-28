def inicio():
    print('\033[33m=' * 60)
    print('MENU PRINCIPAL'.center(50))
    print('=' * 60)
    print('\033[34m1\033[m - \033[35mCadastrar nova pessoa\033[m')
    print('\033[34m2\033[m - \033[35mVer pessoas cadastradas\033[m')
    print('\033[34m3\033[m - \033[35mSair do Sistema\033[m')
    print('\033[33m=\033[m' * 60)

def escolha():
    while True:
        try:
            escolha = int(input('Sua escolha: '))
            while escolha > 3 or escolha < 1:
                print('\033[31mValor digitado não condiz com a tabela\033[m')
                escolha = int(input('Sua escolha: '))
                if escolha > 3 and escolha < 1:
                    break
        except:
            print('\033[31mValor digitado não condiz com a tabela\033[m')
        else:
            break
    return escolha

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except (FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve algum erro')

def opcao1(arquivo) :
    print('\033[33m-' * 60)
    print('CADASTRAR PESSOA'.center(50))
    print('\033[33m-\033[m' * 60)
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('Arquivo não conseguiu ser aberto')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Não consegui computar')
        else:
            print('Pessoa cadastrada com sucesso!')
            arquivo.close()


def opcao2(nome):
    print('\033[33m-' * 60)
    print('LISTA DE PESSOAS'.center(50))
    print('\033[33m-\033[m' * 60)
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Arquivo não conseguiu ser aberto')
    else:
        print('...')
        print(f'Nome                           Idade')
        print('-' * 60)
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        arquivo.close()