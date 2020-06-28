from ex115Library import home
from time import sleep

# SERVE PARA VER SE O ARQUIVO EXISTE E SE N EXISTE CRIAR ELE
arquivonome = 'ex115List'
arquivoExistePrincipal = home.arquivoExiste(arquivonome)
if arquivoExistePrincipal is False:
    home.criarArquivo(arquivonome)
    print('Arquivo não existe')
else:
    print('Arquivo existe')



# TODO O DESENVOLVIMENTO DO SISTEMA
while True:
    home.inicio()
    escolhaPrincipal = home.escolha()
    if escolhaPrincipal == 1:
        # ADICIONAR UMA PESSOA
        home.opcao1(arquivonome)
        sleep(2)
    elif escolhaPrincipal == 2:
        # MOSTRAR LISTA
        home.opcao2(arquivonome)
        sleep(1)
    elif escolhaPrincipal == 3:
        #FINALIZAR PROGRAMA
        print('\033[36m=' * 60)
        print('SAINDO DO SISTEMA'.center(50))
        print('=' * 60)
        break
