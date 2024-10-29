from validação_de_dados import menu

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro em ler o arquivo!!!')
    else:
        menu.titulo("PESSOAS CADASTRADAS")
        for linhas in a:
            dados = linhas.split(';')
            dados[1]= dados[1].replace('\n','')
            print(f'{dados[0]:<30}{dados[1]:>3} Anos.')
    finally:
        a.close()

def cadastra(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print('Novo registro adicionado com sucesso!')
            a.close()