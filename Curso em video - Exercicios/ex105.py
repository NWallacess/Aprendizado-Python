#funções
def nota(*num, sit=False):
    '''
    >Função para analisar notas e situações de varios alunos.
:param *num: uma ou mais notas do alunos(aceita várias)
:param sit: valor opcional indicando se deve ou não adicionar a situação.
:return: dicionario com varias informações sobre a situação da turma.
    '''
    dic={'Total' : 0 , 'Maior': 0, 'Menor': 0, 'Media': 0}
    dic['Media'] = sum(num)/len(num)
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    if sit == True:
        if dic['Media'] >= 7:
            dic['Situação'] = 'Aprovado'
        elif dic['Media'] >= 5:
            dic['Situação'] = 'Recuperação'
        else:
            dic['Situação'] = 'Reprovado'
    return dic       


#Codigo principal
res = nota(3,7,sit=True)
aluno2 = nota(3,4,5,10,sit=True)
print(res)
print(aluno2)
help(nota)