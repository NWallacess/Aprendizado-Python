# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


def menu():
    print("""Selecione o número da operação desejada: 
          
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
""")

soma = lambda a,b: a + b    
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
def divisao(a,b):
    if b == 0:
        print("Aconteceu um erro aqui!")
    else:
        return a/b


while True:
    menu()
    opção = input("Digite sua opção (1/2/3/4/5): ")
    if opção == 1 :
        a = input("Insira o primeiro o valor: ")
        b = input("Insira o segundo o valor: ")
        valor = soma(a=a, b= b)
        print(f"O soma dos valores é igual {valor}")
    elif opção == 3:
        a = input("Insira o primeiro o valor: ")
        b = input("Insira o segundo o valor: ")
        valor = multiplicacao(a=a, b= b)
        print(f"O multiplicação dos valores é igual {valor}")
    elif opção ==2:
        a = input("Insira o primeiro o valor: ")
        b = input("Insira o segundo o valor: ")
        valor = multiplicacao(a=a, b= b)
        print(f"O multiplicação dos valores é igual {valor}")
    elif opção ==4:
        a = input("Insira o primeiro o valor: ")
        b = input("Insira o segundo o valor: ")
        valor = divisao(a=a, b= b)
        print(f"O divisão dos valores é igual {valor}")
    elif opção == 5:
        break
    else:
        print("ERRO!!! Digite uma opção valida. ")