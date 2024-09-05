from modulos import menu, arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    arquivo.criarArquivo(arq)

while True:
    opção = menu.menu(['\033[1;34mVer pessoas cadastradas.\033[m','\033[1;34mCadastrar nova Pessoa.\033[m','\033[1;34mSair do Sistema.\033[m'])
    if opção == 1:
        arquivo.lerArquivo(arq)
        continue
    elif opção == 2:
        menu.titulo('NOVO CADASTRO')
        nome = input('Nome: ').strip().capitalize()
        idade = menu.leiaint('Idade: ')
        arquivo.cadastra(arq, nome, idade)
        continue
    elif opção == 3:
        break
    else:
        print('ERRO!!! Digite uma opção valida.')
        continue
    sleep(1)